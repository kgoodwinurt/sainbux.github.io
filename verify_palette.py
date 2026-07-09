import asyncio
from playwright.async_api import async_playwright
import os
import subprocess
import time

async def verify():
    # Start local server
    server = subprocess.Popen(["python3", "-m", "http.server", "8000"])
    time.sleep(2)  # Give server time to start

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            # --- Test index.html ---
            await page.goto("http://localhost:8000/index.html")

            # Check a.btn color
            btn_color = await page.evaluate("getComputedStyle(document.querySelector('a.btn')).backgroundColor")
            print(f"Index - Button color: {btn_color}")
            assert btn_color == "rgb(0, 123, 189)" # #007bbd

            # Check social icons
            social_links = page.locator("#contact .social-icon")
            count = await social_links.count()
            print(f"Index - Social links count: {count}")
            assert count == 4

            for i in range(count):
                link = social_links.nth(i)
                aria_label = await link.get_attribute("aria-label")
                rel = await link.get_attribute("rel")
                print(f"Index - Social link {i} aria-label: {aria_label}, rel: {rel}")
                assert aria_label is not None
                assert "me" in rel
                assert "noopener" in rel
                assert "noreferrer" in rel

            # --- Test about.html ---
            await page.goto("http://localhost:8000/about.html")

            # Check a.btn color (if exists)
            btn = await page.query_selector('a.btn')
            if btn:
                btn_color_about = await page.evaluate("getComputedStyle(document.querySelector('a.btn')).backgroundColor")
                print(f"About - Button color: {btn_color_about}")
                assert btn_color_about == "rgb(0, 123, 189)"
            else:
                print("About - No a.btn found (skipping color check)")

            # Check Research link
            research_link = page.locator("nav a:has-text('Research')")
            href = await research_link.get_attribute("href")
            print(f"About - Research link href: {href}")
            assert href == "index.html#research"

            # Check social icons in about
            social_links_about = page.locator("#contact .social-icon")
            count_about = await social_links_about.count()
            print(f"About - Social links count: {count_about}")
            assert count_about == 4

            await browser.close()
            print("Verification successful!")

    finally:
        server.terminate()

if __name__ == "__main__":
    asyncio.run(verify())

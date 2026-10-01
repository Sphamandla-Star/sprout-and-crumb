# Sprout & Crumb — Website Guide

This is the guide for your bakery website. You don't need to know anything about code to use it. Every section below explains what part of the site does what, and exactly how to make common changes like updating a price or adding a new item.

---

## What's in the file

Your entire website lives in one file called **`index.html`**. To edit it, open the file in any plain text editor (Notepad on Windows, TextEdit on Mac — but make sure TextEdit is set to plain text, not rich text). Do **not** open it in Word, as Word will corrupt the file.

---

## Sections of the site

### 🌿 Today's Special banner
The thin green strip at the very top of the page. It shows a special item and its price.

**To change it**, find this line near the top of the file:
```
🌿 <strong>Today's Special:</strong> Cardamom &amp; Orange Blossom Cake — £20.00 &nbsp;·&nbsp; Pre-order yours below!
```
Replace `Cardamom &amp; Orange Blossom Cake` with your new item name, and replace `£20.00` with the new price. Leave everything else exactly as it is.

> **Note:** If your item name contains an `&` (ampersand), type `&amp;` instead — for example, "Lemon &amp; Ginger" not "Lemon & Ginger". This is a quirk of how websites work.

---

### 🍞 Navigation bar
The dark bar that sits just below the Today's Special banner, with links to Menu, Our Story, and Pre-Order. You do not need to change this unless you rename a section of the site.

---

### 🌾 Hero (the big welcome banner)
The large section at the top with your bakery name and the "Pre-Order Now" button. The tagline currently reads:

> *Freshly baked. Entirely plant-based.*

**To change the tagline**, find:
```
<p>Freshly baked. Entirely plant-based.</p>
```
Replace the words between `<p>` and `</p>` with your new tagline.

---

### 🥐 Menu
This section shows all your baked goods, grouped into three categories: **Breads**, **Cakes**, and **Pastries**.

#### How to change a price
Find the item by its name. Just below it you will see a price that looks like this:
```
<span class="price">£4.50</span>
```
Replace `£4.50` with your new price. Leave the `<span class="price">` and `</span>` tags exactly as they are.

#### How to change an item's name or description
Each item looks like this:
```
<h4>Seeded Sourdough</h4>
...
<p>A slowly fermented loaf with sunflower and pumpkin seeds...</p>
```
Replace the text between the tags with your new name or description.

#### How to change the dietary tags (Vegan, GF, NF)
Each item can have tags like `Vegan`, `GF` (gluten-free), or `NF` (nut-free). They look like this:
```
<span class="tag">Vegan</span>
<span class="tag">NF</span>
```
You can delete a line to remove a tag, or copy a line and change the word to add a new one.

#### How to add a brand-new menu item
Find the category you want to add to (Breads, Cakes, or Pastries). Inside that category, copy an entire block that starts with `<div class="menu-card">` and ends with the matching `</div>`, then paste it just before the `</div>` that closes the menu grid. Update the name, price, description and tags to match your new item.

#### How to add a new category
Copy an entire `<div class="menu-category">` block (from the opening `<div class="menu-category">` to its closing `</div>`) and paste it after the last category. Change the `<h3>` heading to your new category name, then update the items inside it.

---

### 📖 Our Story
A section with a photo and three paragraphs about you and your bakery.

**To change the text**, find the `<section id="story">` part of the file. The three paragraphs each start with `<p>` and end with `</p>`. Replace the words inside them with your own.

**To change the photo**, find:
```
<img
```
followed by a long `src="..."` web address. Replace that address with the web address of your own photo, or ask your web developer to swap it in.

---

### 📋 Pre-Order form
The form customers fill in to place an order. It collects:
- Name, email, and phone number
- What items they want and how many
- A collection date (Tuesday–Saturday only, and at least 48 hours from the day they're ordering) and time
- Optional dietary notes and a personal message

The form automatically checks that customers fill it in correctly before they can submit it. You do not need to change anything here unless your collection days or notice period change — for those, ask a developer.

**To change the collection notice text** (currently "at least 48 hours' notice"), find:
```
Please give us at least <strong>48 hours' notice</strong>.
```
Change `48 hours` to whatever your policy is.

**To change the collection days** (currently Tuesday–Saturday), find:
```
Collection is available <strong>Tuesday – Saturday</strong>.
```
Update the days to match your actual hours.

---

### 🦶 Footer
The dark bar at the bottom of the page with your opening hours and copyright.

**To update your opening hours**, find:
```
<p>Open Tuesday – Saturday &nbsp;|&nbsp; Hours TBC</p>
```
Replace `Tuesday – Saturday` and `Hours TBC` with your real days and times.

---

## Quick-reference: the most common tasks

| What you want to do | What to look for in the file |
|---|---|
| Change Today's Special | Find `Today's Special:` |
| Change a price | Find the item name, then change the `£` amount below it |
| Change an item description | Find the item name, then change the text between `<p>` and `</p>` |
| Add or remove a dietary tag | Find the item name, then edit the `<span class="tag">` lines |
| Update opening hours | Find `Open Tuesday – Saturday` |
| Change collection days in the form | Find `Collection is available` |

---

## A note on saving and testing

After making any change, save the file, then open it in a web browser (double-click it, or drag it into Chrome or Firefox) to check everything looks right before publishing it live.

If anything breaks, undo your change (`Ctrl + Z` on Windows, `Cmd + Z` on Mac) or reach out to your developer.

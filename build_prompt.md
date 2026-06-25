# H5 Project Build Task - 最长白昼，留给最亲的人

You are building a mobile H5 web app for a Father's Day marketing campaign. All assets and stories are ready.

## Project Location
- Working directory: /home/wlll_agent/H5_code
- All assets are at: assets/images/types/
- Stories data file: 最长白昼_24个故事初稿.md

## Tech Stack
- Pure HTML + CSS + JavaScript (single-page app)
- No frameworks, no external libraries
- Mobile-first, responsive design
- All images relative paths from assets/images/types/

## Image Naming Convention
Each folder under assets/images/types/ is a story category (肩背型, 手艺型, 接送型, etc.)
Each story has: story{1|2|3}_act{1|2|3}_{keyword}.png
- act1 = childhood memory scene (768x1024, warm watercolor, top 40% empty for text)
- act2 = current change scene (768x1024, warm-cool watercolor, top 40% empty for text)  
- act3 = object close-up (768x768, clean background, product shot)

## Design Style
- Watercolor illustration style throughout
- Warm, muted tones (amber, beige, soft grey)
- No photos, only watercolor-style illustrations
- Soft, nostalgic, quiet mood
- Font: system sans-serif, clean and readable

## Page Architecture (5 pages + 1 popup)

### P1 - Home Page (5-screen scroll)
Screen 1: Full-screen cover with title "最长白昼，留给最亲的人", date "2026.6.21 夏至·父亲节", warm gradient background (use 肩背型/story1_act1_fireworks.png as hero image), downward scroll hint
Screen 2: Manifesto - 3-4 lines of short text, large typography, white space, watercolor texture background
Screen 3: Story stream - 8 category filter tabs that become sticky at top, story cards x3 visible at a time, single vertical column (not waterfall), cards show thumbnail (use act1 image) + title + one-line summary
Screen 4: Story stream continued + data wall (static data display: 24个家庭·5座城市·8种父亲, counter placeholders)
Screen 5: Entry area + Footer - "写我的故事" button (→P4), "留言墙" button (→P3), copyright info

### P2 - Story Detail Page (4-screen scroll, navigated from P1)
Screen 1: Act 1 - Childhood memory: full-width act1 image as background, story title + act1 text overlaid on top portion (text readable on the warm toned image)
Screen 2: Act 2 - Current changes: full-width act2 image as background, act2 text overlaid
Screen 3: Act 3 - Object: act3 image displayed prominently (square), object name, "替我也送一份" button that triggers expand layer below (不跳转，向下展开)
Screen 4: Interaction area - single story comments, related story recommendations (horizontal scroll cards), share button

### Expand Layer (inside P2 screen 3, not a page jump)
- Object watercolor image (reuse act3 image)
- Emotional connection sentence from the story
- Price range in grey small text
- Button: "去京东看看" (NOT "立即购买")
- Collapsible with × button
- Smooth watercolor transition animation

### P3 - Message Wall (from P1 screen 5)
- Two-column waterfall layout
- Each message tagged with source story
- Click message to jump to corresponding P2
- Bottom sticky button "也写一个你的故事→" → P4

### P4 - UGC Form (2 screens)
- Screen 1: Guide copy + exemplary UGC example + 8 category tag selector
- Screen 2: Form: childhood memory, current change, object thought (optional), nickname, submit
- Key: any single act can be submitted (low barrier)
- Post-submit: "你的故事已收到" (not immediately published, needs review)

### P5 - Share Card (popup layer, 4:5 vertical)
- Top: story act1 image thumbnail
- Middle: story title + one-line summary
- Bottom: "最长白昼，留给最亲的人" + "京东" branding
- Auto-generated, savable to album, shareable to WeChat/Weibo
- Bottom has QR code placeholder area

## Stories Data

The 24 stories are organized into 8 categories, each with 3 stories. Each story has 3 acts (text) and 3 images.

Read the full stories from: /home/wlll_agent/H5_code/最长白昼_24个故事初稿.md

The 8 categories and their image folders:
1. 肩背型 → assets/images/types/肩背型/
2. 手艺型 → assets/images/types/手艺型/
3. 接送型 → assets/images/types/接送型/
4. 厨房型 → assets/images/types/厨房型/
5. 沉默型 → assets/images/types/沉默型/
6. 让步型 → assets/images/types/让步型/
7. 等待型 → assets/images/types/等待型/
8. 转身型 → assets/images/types/转身型/

## Mobile UX Requirements
- Return to P1 preserves scroll position (use sessionStorage)
- Screen transitions with watercolor dissolve animation
- Category filter: fade in/out cards without page refresh
- Lazy load images (WebP or compressed PNG)
- First screen loads only hero image
- Virtual list for message wall
- Share card pre-generated when user enters P2

## Story Card Data Format
Each card needs: category name, story title, 3 acts text, emotional connection sentence, 3 image paths

## Output Files
Create a single HTML file: index.html
With all CSS embedded and JavaScript embedded.
The file should work by simply opening it in a mobile browser.

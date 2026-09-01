---
title: "Canvas UI Widget"
sidebar_position: 2
---

<show-structure />

We need to show the minimap in your screen. Create a new UMG User widget (or open an existing one) and drag drop the `Dungeon Canvas Widget` on to the screen

Turning the minimap into a full screen, pannable and zoomable map

<iframe
    width="100%"
    height="540"
    src="https://www.youtube.com/embed/qmYAaofChWQ"
    frameBorder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowFullScreen
/>

![image|622x499](../images/unreal/tutorial/Canvas/1e7377e11cc6f99d7befa4dda9b624481e0e19d2.png)


Select the widget and check the details panel .  Expand the `Draw Setttings`:

![image|690x430](../images/unreal/tutorial/Canvas/d0a7fb75acb263991fdd8c6f57fdd83cf4f7d1bf.png)

You can control various settings from here:

---

**`Rotate to View`**:    This will rotate the minimap and the player icon will be fixed.  uncheck to keep the view fixed and have the player icon rotate

![image|690x388](../images/unreal/tutorial/Canvas/88baaacad9c75b4c468ce59333710bc598e23b59.jpeg)

---
**`Base Canvas Rotation`**: You may want the whole view to be rotated by a certain amount.    Unreal defaults to the character facing the X direction. so if this is 0, it looks like this with the `rotate to view` flag enabled (red player arrow always faces right and everything rotates around it):

![image|518x48](../images/unreal/tutorial/Canvas/152de8d4c7bee728f93aa1ce2acc02f565566ab5.png)

![image|492x500](../images/unreal/tutorial/Canvas/707d30381c6406468b8365f6c8b38bd052180adf.jpeg)

If you want the arrow to face up (while the world rotates around it, rotate the whole view by 90

![image|564x209](../images/unreal/tutorial/Canvas/6552adfcf6bc4be640754bf4950906a9ec59e805.png)

![image|565x500](../images/unreal/tutorial/Canvas/5fbabd12b60963c6c48e7f1a3a6f16dde5932dec.jpeg)


---

**`Fog of War Enabled`**: Check this to enable Fog of War. If you have this enabled, you need to setup your player to be a fog of war "explorer" so parts of the map can be made visible as you explore (more on that later below). You can have multiple explorers.

![image|690x349](../images/unreal/tutorial/Canvas/1ae1a6e7e2e3cf79e48c3ec98c0dfcf7fbf534a8.jpeg)

---

**`Fog of War Fully Explored`**:  Enable this if you want the whole map explored. You may still enable fog of war to show the visible areas.

![image|462x500](../images/unreal/tutorial/Canvas/cf1875a97035421dbb3baabd09b12b5c57e39541.jpeg)


With and without Fog of War enabled:

![image|269x500](../images/unreal/tutorial/Canvas/6b4535380121062b060fe00accff9ea4e29457b0.jpeg)

> Note: You can configure NPC icons to show up only on the visible (bright) areas

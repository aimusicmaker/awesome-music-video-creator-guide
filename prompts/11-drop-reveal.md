# 11 · Chorus color change

[All recipes](README.md) · [Home](../README.md) · [Editing help](../docs/editing.md)

**Level:** Intermediate · **Editing target:** 16 seconds · **Status:** original brief, not render-tested.

## Bring these inputs

A track with a marked chorus/drop and two compatible reference images.

**Starting route:** [Short Music Video Generator](https://musicmaker.im/free-short-music-video-generator/). Use only input modes and durations currently offered by the tool. Longer plans require separate clips and editing.

## Image direction

Use this to create or choose a reference image. For text-to-video, the motion prompt can be used without an image when the tool permits it.

```text
One folded paper lantern centered in a dim navy room. Make a second reference with the same lantern glowing warm amber, identical camera, size and backdrop.
```

## Copy the motion prompt

```text
The paper lantern remains centered and keeps its folded shape. A gentle warm light grows inside it. Locked camera, unchanged room, no extra objects, no flying paper, no text.
```

## Copy one prompt per shot

Use the same reference image or reference sheet when supported. Each block below is a complete prompt for **one separate generation**. Timings describe the edit, not the generation request; generate a supported length and trim it.

<details>
<summary>Opening detail</summary>

```text
Close view of folded paper on one unlit lantern in a dim navy room. Fixed camera, faint cool light, unchanged folds. No new props or text.
```

</details>

<details>
<summary>Before the chorus</summary>

```text
One folded paper lantern centered in a dim navy room, unlit. Locked wide camera, stable paper shape and room, no motion except faint ambient dust, no text.
```

</details>

<details>
<summary>At the chorus</summary>

```text
The same folded paper lantern, centered at the identical scale in the same navy room, now glowing steadily amber from inside. Locked camera, stable folds, no flash, no extra objects or text.
```

</details>

<details>
<summary>Closing hold</summary>

```text
Hold the same wide composition of one amber-lit paper lantern in the navy room. Stable exposure and paper folds, no new movement or text. Leave a quiet area for an editor-added title.
```

</details>

## Music direction

For an original song or instrumental; skip this if you already have audio.

```text
Instrumental pop/electronic cue: restrained opening, a clear rhythmic lift, then a settled groove. Mark the real change after generation rather than assuming it occurs at a requested second.
```

## Assemble the edit

Generate the four shot prompts above separately. For the practice beat, trim each to four seconds: opening detail at 0:00, dim wide at 0:04, lit wide at 0:08, closing hold at 0:12. Match framing between the dim and lit wide views. For your own song, move the reveal to its actual chorus marker.

## If it fails

If the lighting change misses the beat, adjust the edit, not the whole generation. If folds deform, use two stills with a crossfade instead.

**Before you export:** There is one clear reveal; the important moment is understandable even without extra effects.

Change one variable per retry and keep your best take. Use the [brief template](../starter-kit/brief-template.md) to record the actual inputs, output settings, and changes.

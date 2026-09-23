# 10 · One prop, three worlds

[All recipes](README.md) · [Home](../README.md) · [Editing help](../docs/editing.md)

**Level:** Intermediate · **Editing target:** 12 seconds · **Status:** original brief, not render-tested.

## Bring these inputs

One original prop reference and three backgrounds.

**Starting route:** [Short Music Video Generator](https://musicmaker.im/free-short-music-video-generator/). Use only input modes and durations currently offered by the tool. Longer plans require separate clips and editing.

## Image direction

Use this to create or choose a reference image. For text-to-video, the motion prompt can be used without an image when the tool permits it.

```text
A matte red sphere centered on a plinth, sphere diameter one third of image width, eye-level camera. Create three separate stills: studio, desert dusk and foggy forest; preserve sphere position and scale.
```

## Copy the motion prompt

```text
Keep the matte red sphere completely still at the center and preserve its size. Only environmental mist or dust moves gently. Locked eye-level camera. No rotation, deformation, new props or lettering.
```

## Copy one prompt per shot

Use the same reference image or reference sheet when supported. Each block below is a complete prompt for **one separate generation**. Timings describe the edit, not the generation request; generate a supported length and trim it.

<details>
<summary>0–4s · Studio</summary>

```text
One matte red sphere centered on a plinth in a charcoal studio. Sphere diameter is one third of frame width. Eye-level fixed camera. Only faint ambient dust moves; sphere and plinth stay still. No text.
```

</details>

<details>
<summary>4–8s · Desert</summary>

```text
The same matte red sphere centered at the same size on the same plinth, now in a desert at dusk. Eye-level fixed camera. Faint background dust drifts; sphere and plinth stay still. No other props or text.
```

</details>

<details>
<summary>8–12s · Forest</summary>

```text
The same matte red sphere centered at the same size on the same plinth, now in a foggy forest. Eye-level fixed camera. Only background mist moves. Preserve sphere proportions and plinth height, no text.
```

</details>

## Music direction

For an original song or instrumental; skip this if you already have audio.

```text
Minimal rhythmic instrumental: dry kick, ticking percussion and a simple repeating synth motif. Choose three clear phrase starts for the background changes.
```

## Assemble the edit

Generate three independent shots using the same prop reference. Trim each to four seconds. Align the sphere’s center and size with the editor’s position/scale controls before cutting.

## If it fails

If the match feels wrong, fix scale and position first; do not add a transition to hide mismatched geometry. If perspective changes too much, regenerate just that scene.

**Before you export:** The prop appears to stay in place while the world changes around it.

Change one variable per retry and keep your best take. Use the [brief template](../starter-kit/brief-template.md) to record the actual inputs, output settings, and changes.

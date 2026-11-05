# 13 · Ribbon accent: subject motion versus camera motion

[All recipes](README.md) · [Home](../README.md) · [Editing help](../docs/editing.md)

**Level:** Easy · **Editing target:** 8 seconds

**Status: untested brief; not render-tested.** This is an original text-only exercise. No video, audio, reference image or observed failure accompanies it.

## Intended result

Plan an eight-second music visual with two contrasting shots of one blue cloth ribbon against a plain peach backdrop. A cut near a musical accent separates movement of the ribbon from movement of the camera. Eight seconds is an editing target, not a promised generation duration.

## Bring these inputs

- An eight-second excerpt of music you own or may use. Choose the excerpt so that a clear accent falls near its midpoint, or move the proposed cut to an accent you hear.
- Optionally, your own authorized reference image: one blue cloth ribbon suspended from a single hook, centered against a plain peach backdrop. Keep its shape, color and framing consistent across shots.
- A video tool whose current inputs and output lengths you have checked, plus an editor that can trim clips, join them and retain one audio track. No particular tool, model, settings, price or successful output has been tested for this brief.

## Image direction

For an optional reference, create or choose your own authorized image of the single blue cloth ribbon and hook against the peach background. Use eye-level medium framing and soft upper-left light. Keep the reference free of lettering; no third-party image is supplied here. Text-to-video needs no reference image if the chosen tool supports that mode.

## Copy the motion prompt

Use one prompt per separate shot. If using a reference, supply your authorized image through a supported image input; do not assume that naming it in text attaches it.

**Shot A — subject motion, camera still**

```text
One blue cloth ribbon hangs from a single small hook against a plain peach backdrop. Soft light comes from the upper left. Locked eye-level medium shot. The lower end of the ribbon sways slowly from left toward right; the hook and backdrop stay still. Keep one ribbon with the same length and color throughout. No people, lettering, extra objects, cuts or camera movement.
```

**Shot B — subject still, camera motion**

```text
One blue cloth ribbon hangs motionless from a single small hook against a plain peach backdrop. Soft light comes from the upper left. Begin at an eye-level medium framing and move the camera slowly closer. Keep the ribbon, hook and backdrop still; preserve the ribbon's length and color. No people, lettering, extra objects, cuts or sideways camera movement.
```

## Music direction

Use the authorized excerpt you prepared; no music-generation prompt or downloaded song is required. Listen for an accent near the midpoint and mark it in the editor. Move the edit cut to the music rather than assuming that a video generator will synchronize it.

## Assemble the edit

1. Before generating, record the selected tool, input mode, actual offered duration and any cost in the [brief template](../starter-kit/brief-template.md). Stop if the tool cannot accept the required inputs. This exercise does not require a particular provider.
2. If you choose to test the brief, make A and B separately at a supported length. Retain usable portions rather than assuming either requested motion succeeded.
3. Place A before B. Start with a four-second portion of each; move the cut to the chosen musical accent if needed while keeping the eight-second target.
4. Mute generated audio and keep the authorized music excerpt as the single soundtrack. Add any title in the editor, outside the image prompts.
5. If you test the brief, inspect the first two seconds of each shot for the requested change, then review the rendered edit for a clear contrast: in A, the camera stays still while the ribbon moves; in B, the ribbon stays still while the camera moves. Check the cut for unwanted changes in shape, color or lighting, and check that picture and sound finish together.

## If it fails

These are hypotheses, not failures observed in a generated result.

- **Ribbon shape changes during A:** shorten the retained movement or reduce the requested sway, changing only one variable per retry. Compare whether the ribbon keeps its length and remains a single object.
- **Both subject and camera move in B:** try a locked-camera version as a control. If it preserves the subject better, an editor's modest crop animation may provide the push-in, with an acknowledged loss of available framing.
- **The two shots do not match:** compare the starting composition, reference and lighting before changing the transition. Do not describe a matching result until you have inspected the actual files.

Record actual inputs, output dimensions and duration, the changed variable and what happened. A finished plan alone is not a completed or validated video.

## Provenance and disclosure

An AI assistant wrote this original scene, its prompts and edit plan for this proposal. The general prompt-planning framework came from [imgmov's video-prompt guide](https://imgmov.com/blog/2026-07-08-ai-video-prompts), specifically **Product and commerce prompts** and the first three items under **How I test prompts now**. Those sections separate subject action, camera action and light, and supply additional combined-motion examples. This brief turns that framework into an original, untested ribbon contrast; the guide does not document this scene or its outcome. It does not establish that imgmov originated these general principles. The repository's existing recipe and brief-template format also informed this contribution. The article's first-person experience, model-performance, price and credit-saving claims are not adopted.

This proposal is prepared for imgmov's operator as part of its acquisition campaign. The source link has a promotional interest and is not an independent endorsement. No third-party media is included.

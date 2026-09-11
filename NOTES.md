# Notes for Skye — first draft

The page is written to be shown to a prospective employer as it stands. Nothing
on it is invented: every claim is either something you told me, or something I
verified from the gym's own channels (listed at the bottom).

## The six gaps

Six places want a real number or asset that I could not source. They are marked
in the HTML with `class="gap"` and are **hidden in the published page**, so the
site reads as finished.

To see them in place while you fill them in, change the opening tag of
`index.html` to:

```html
<html lang="en-AU" id="top" data-draft>
```

Remove `data-draft` again before publishing. The gaps:

| Section | Needs |
| --- | --- |
| Membership drive events | How many drives a year, typical attendance, conversion to membership |
| Mum's n Bubs | Launch year, typical class size, how long it ran, price point |
| The Push-Up Challenge | Which year(s), team size, amount raised, nominated charity |
| The identity | Logo files, colour and type specs, shopfront signage, merch, print work |
| Closing the doors | The closing date, and how the closure was announced to members |
| Get in touch | Email, phone, LinkedIn |

## Decisions to confirm

- **Voice.** First person ("I ran the brand…"). Third person is a one-pass change.
- **Mat.** The page says "my husband coached" without naming him. Say if you want him named.
- **Follower counts.** The page says "roughly two thousand" (Instagram) and "thirteen
  hundred" (Facebook). Those are figures readable today from dormant accounts, so they
  are close to but not exactly the 2021 numbers — which is why the copy keeps them
  approximate. The 1,007 post count is effectively final and is stated exactly.
- **"Perth's first dedicated calisthenics and bodyweight gym"** is stated as fact. It is
  the business's own positioning line, used on the Facebook page. Fine to keep unless you
  would rather soften it.
- **The Push-Up Challenge** is the one project with no public trace I could find — no team
  or fundraiser page survives under the gym's name. The copy therefore describes what you
  did without citing figures. The campaign facts quoted (3,046 in 2020; 3,318 in 2021) are
  sourced and correct.

## Verified from the gym's own channels

Gathered with a headless browser, since both platforms block ordinary fetching.

**Business**
- 11/83 Hector St W, Osborne Park, WA 6017
- Facebook intro: "Perth's first dedicated Calisthenics and Bodyweight Gym"; category "Coach"
- Facebook: ~1.3K followers, 100% recommend from 6 reviews
- Old site strapline: "a class and person training calisthenics studio offering bodyweight
  strength, mobility and handbalancing coaching"
- Both domains (thebodyweightgym.net, .com.au) are now deleted

**Instagram @the_bodyweight_gym**
- 1,007 posts; last activity September 2021
- Bio: group bodyweight classes, group mobility classes, hand balancing, personal training,
  remote coaching — "2 WEEK FREE TRIAL, follow linktree !"
- Story highlights: Timetable, Students, Classes, Class Program, Equipment

**People named in posts**
- Coaches: Ana (calisthenics), Maisie (mobility), Corey, Matt
- Online roster, Nov 2020: Maisie, Oscar, Corey, Mikhail, Ray, Kelvin
- Members featured by name: Dustyn

**Named formats**
- Social Saturday — 8am calisthenics with Ana, 9am mobility with Maisie
- Wednesday night strength with coach Matt
- Monday morning bodyweight/calisthenics and Friday morning handstand, both with Corey
- Mum's n Bubs with Corey

**Mum's n Bubs — the source for that case study** (Instagram, 18 June 2021)
> "Here we have our Mum's n Bubs class with coach Corey! I've spoken to a handful of parents
> who assumed the Mum's n Bubs class was a class where mother's used a baby as a weight for
> exercise! No not quite! In fact it's simply a class where parents can bring their toddlers,
> and feel supported that everyone there can feel comfortable and without pressure. It's not
> only limited to mother's though! And Eva's dad Sean trains today while Sky and Eva do
> drawing in their cubby."

**The online pivot** (Facebook, 2 November 2020)
> "The Bodyweight Gym Online … NEW CLASSES ADDED. We have added another 7 hours of
> follow-along class content for you to enjoy free* … *for a limited time while we are in
> development"

**The closure** — the final line left on the website, quoted on the page:
> "We have closed - thankyou to all our members that made the gym what it was!"

**Context**
- WA closed gyms in late March 2020 and permitted reopening in June 2020
- The Push-Up Challenge: founded Perth 2017 by Nick Hudson; 2019 target 3,128 over 21 days
  (headspace); 2020 target 3,046, 11–31 May (headspace); 2021 target 3,318, 1–25 June
  (headspace, Lifeline or Push for Better)

## Images

19 images are in `assets/img/`, pulled from the gym's own Instagram: twelve posts from
August–September 2021, five story-highlight covers, and two in-gym photographs. All are
square 640px except the two photographs.

Anything else worth adding — logo files, signage, merchandise, event photos, Mum's n Bubs
artwork — drops into `assets/img/` and can go in as another `<figure class="exhibit">`.

## Running it

Static site, no build step, no dependencies.

```
python3 -m http.server 8000
```

Then <http://localhost:8000>. To publish: Settings → Pages → deploy from branch, root.

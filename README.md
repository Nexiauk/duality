# Duality: Legends Unchained

![Am I responsive](../duality/docs/screenshots/amiresponsive.jpg)

[View the live project here](https://duality-2411f10ea2e4.herokuapp.com/)

This app has been created as a project during my [Code Institute](https://codeinstitute.net/) Level 5 Web App Development course.

## Table of Contents

- [Duality: Legends Unchained](#duality-legends-unchained)
- [Duality Blurb](#duality-blurb)
- [Inspiration](#inspiration)
  - [Reluctant Readers](#reluctant-readers)
  - [The Psychology of Collecting](#the-psychology-of-collecting)
  - [The Idea](#the-idea)
- [Goals](#goals)
- [User Experience (UX)](#user-experienceux)
  - [Types of Users](#types-of-users)
  - [User Stories](#user-stories)
    - [Guest Users](#guest-users)
    - [Registered Users](#registered-users)
    - [Admin Users](#admin-users)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Colour Palette](#colour-palette)
  - [Colour Accessibility](#colour-accessibility)
  - [Imagery](#imagery)
  - [Typography](#typography)
  - [Wireframes](#wireframes)
  - [End Product Design Changes](#end-product-design-changes)
- [Features](#features)
  - [Users](#users)
  - [Characters](#characters)
    - [Archetype Mapping Logic](#archetype-mapping-logic)
    - [Quantitative Criteria Key](#quantitative-criteria-key)
    - [Interpretation Notes](#interpretation-notes)
  - [Cards](#cards)
  - [Responsiveness](#responsiveness)
  - [Header](#header)
  - [Footer](#footer)
  - [Home Page](#home-page)
  - [Shop Page](#shop-page)
  - [Binder Page](#binder-page)
  - [Profile Page](#profile-page)
  - [Admin](#admin)
- [Security Features](#security-features)
  - [Authentication & User Management](#authentication--user-management)
  - [Access Control](#access-control)
  - [Permissions & Roles](#permissions--roles)
  - [Environment Variables](#environment-variables)
  - [Deployment Security](#deployment-security)
  - [Payment Security](#payment-security)
- [Future Features](#future-features)
- [Models and Data Relationships](#models-and-data-relationships)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Overview](#overview)
  - [Model Relationships (ERD Notation)](#model-relationships-erd-notation)
  - [Model Fields](#model-fields)
- [Testing](#testing)
  - [User Story Testing](#user-story-testing)
  - [Automated Testing](#automated-testing)
  - [Manual Testing](#manual-testing)
  - [Unit Testing](#unit-testing)
- [Technology Used](#technology-used)
- [Coding Help](#coding-help)
- [Interesting Bugs](#interesting-bugs)
- [Deployment](#deployment)
- [Credits](#credits)


## **Duality Blurb**
The barriers between universes have collapsed - chaos reigns!

Step into the multiverse and collect Heroes and Villains from across realities.  
Build your top-secret binder of champions and decide your path:

Assemble a force for light to restore balance, or

Embrace the darkness and command chaos.

Duality: Legends Unchained is a collectible card app where you curate your ultimate team from across your favourite universes.

## **Inspiration**

### *Reluctant Readers*
My son is what schools call a “reluctant reader.” If a book doesn’t have illustrations, he simply isn’t interested, no matter how much he’s encouraged. But give him something with pictures and you can’t stop him. He’s read and re-read every Diary of a Wimpy Kid, Tom Gates, Louie Stowell’s Loki series, Bunny vs Monkey, Donut Squad — the list goes on. His shelves are overflowing with graphic novels: Harley Quinn, Deadpool and Venom comics, and yet he’s still labelled as reluctant, simply because his reading is visual.  
Illustrated storytelling is not a crutch, it’s a gateway. Graphic novels and comics can pave a prettier pathway into reading for pleasure, especially for readers who find long blocks of text daunting.

### *The Psychology of Collecting*
At the same time, I’ve seen how collecting hooks people in. My brother, for example, has a Pokémon card binder, ostensibly ‘for his son’ — but I remember him collecting the same cards as a kid. It’s not really about resale value. It’s about the joy of owning something rare, of filling pages, of seeing a collection grow and feeling proud of it. That psychology is powerful, especially when paired with storytelling.

### *The Idea*
Originally, I wanted to make a fairy-tale inspired card collection with characters and objects from classic stories with the idea being that the visual nature of the cards would be appealing to reluctant readers, who would then learn a little more about those stories after purchasing the cards. But when I started designing the cards, I realised the scope was bigger than I could handle. So I stepped back and looked for data sources that could bring a ready-made universe to life. 

That’s when I stumbled across the [Superhero API](https://www.superheroapi.com/). It collates 731 heroes and villains from across different publishers and universes. Superheroes and villains never really go out of fashion — they just get remade, recast, and reimagined for new audiences. By combining this treasure trove of illustrated characters with the psychology of collecting, and framing it in a narrative about collapsed multiversal barriers, Duality: Legends Unleashed was born.  

It’s not just about collecting cards. It’s about creating your own super-powered team — heroes or villains — and, maybe along the way, finding that illustrated storytelling can make reading fun again.

## **Goals**
* Build an addictive, card-collecting experience.  
* Display hero and villain cards in a top secret binder.  
* Inspire reading through illustrated biographies.  
* Enrich content with diverse characters curated by experts.  
* Promote exploration, discovery, and replay.

## **User Experience(UX)**

### *Types of Users*

* Adults who enjoy collectibles  
* Children who enjoy collectibles  
* Anyone who enjoys Heroes/Villains  
* Anyone who enjoys ‘visual’ reading  
* Guests who want to browse  
* Registered users who want to collect  
* Admin who curate the content

### *User Stories*

#### **Guest Users**

*As a guest I want to:*

**Account / Access**

* **Browse** the site using simple, logical, clear navigation so that I can find out what it’s about.

* **Easily find** a sign-up button, so that I can sign up to become a ‘collector’ (customer).

* **Register** for an account using a logical, clearly-defined form, so that I can start building my collection.

---

#### **Registered Users**

*As a registered user I want to:*

**Account Management**

* **Find a login/logout button**, so that I can quickly sign in with minimal effort.

* **Change my password and email address**, so that I can keep my account secure and receive payment receipts.

**Shop Interaction**

* **Browse the available cards in the shop**, so that I can decide which ones to collect.

* **Filter the available cards in the shop**, so that I can easily locate heroes/villains of specific types for my collection.

* **See at a glance which cards are free and which ones require payment**, so that I can make quick decisions on which cards to collect.

* **See at a glance the different card rarities and Universes**, so I can make informed collection decisions.

* **See at a glance and easily use a 'Buy Now' button**, so I can efficiently make a purchase.

* **Be given the option to continue or cancel my purchase**, so I can change my mind if I want.

**Binder / Collection Management**

* **Add free cards to my binder with a single click**, so that I can build my collection quickly and efficiently.

* **Add purchasable cards to a basket with a single click**, so that I can efficiently purchase them if under time constraints.

* **Cancel my purchase before it’s processed**, so that I have the option to change my mind.

* **Access a binder of my collected cards**, so that I can view my purchases and their additional unlocked content.

* **Filter or search my binder,** so that I can quickly view cards by type, rarity, or attributes (Hero, Villain, Universe, Power Rating).

**Payments & Feedback**

* **Make secure payments through Stripe**, so that I can purchase cards without worrying about payment safety.

* **See immediate visual cues, like animations or highlights, when I add cards to my basket or binder**, so that I know my actions have been registered.

---

#### **Admin Users**

*As admin I want to:*

**Collection Management**

* **See all cards in the Master Collection**, so that I can easily review and edit their content.

* **Add new cards to the Master Collection**, so that customers have more cards to collect.

* **Filter the Master Collection by Rarity and Universe**, so that I can easily find and manage specific cards and their sub-collections.

**Shop Management**

* **See what cards are currently marked for shop rotation**, so I can add and remove to the rotation as desired.

* **Schedule shop rotations and set/adjust the shop refresh schedule**, so that new card batches appear at predictable times or immediately when needed.

* **Set price bandings based on a card’s power rating**, so that cards of higher rarity automatically have higher prices and shop pricing remains consistent.

* **Adjust the prices for each rarity band or individual card**, so that I can control the shop economy and run promotions without changing the underlying card power ratings.

* **Set card availability**, so that I can control which cards are on sale or temporarily removed from the shop, supporting special offers and promotions.

**User Management**

* **See a list of all registered users**, so that I can support accounts as needed.

* **Track purchase history**, so that I can troubleshoot issues and handle refunds.

**Payments & Security**

* **Manage Stripe payment settings and view transaction logs**, so that I can ensure secure and smooth payments.

* **Back up the Master Collection and user data**, so that content is safe in case of system failure.

## **Design**

### *Colour Scheme*
I was inspired by [this Bootstrap Theme](https://bootswatch.com/quartz/) \- the gradient background gives off a duality vibe and the glassmorphism effect is futuristic, as well as emphasising light or dark objects placed on top of colorful backgrounds. Ideal for highlighting the contrast between the heroes and the villains. This theme gave me the idea of a progress meter tied to the background gradient colour, so the more hero cards that are collected, the lighter the background, the more villains, the darker it gets.

### *Colour Palette*
In comic books, superheroes used to be depicted in primary colours (Red, Blue, Yellow) due to primary colours being easier to print in the four-colour printing process. As villains appeared on the strips less often than their heroic counterparts, they were allocated the secondary colours (Green, Purple, Orange). 

[Superhero Colour Theory](https://comicsalliance.com/superhero-color-theory-primary-heroes/)  
[Colouring Comics, Old School](https://kleinletters.com/Blog/coloring-comics-old-school/)

The famous photograph “Lunch Atop Skyscraper” has a version that replaces the workers with Marvel and DC characters. I used [Adobe Color](https://color.adobe.com/) to generate a palette from a portion of that image where the colours are representative of old school comic hero and villain colours. I manually grabbed yellow from the image.  

![Lunch Atop Skyscraper colour palette](../duality/docs/screenshots/colour-palette.png)

#A6121F - Ecstatic Red  
#845ABF - Fuchsia Blue  
#AAB1BF - Eclectic  
#2182BF - Skylla  
#88A649 - Nasturtium Shoot   
#D9A404 - Vivid Yellow

### *Colour Accessibility*
I used [Eight Shapes Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=%23845ABF%0D%0A%23AAB1BF%0D%0A%232182BF%0D%0A%2388A649%0D%0A%23A6121F%0D%0A&foreground-colors=%23000000%0D%0A%23ffffff%0D%0A%23AAB1BF%0D%0A%23845ABF%0D%0A%232182BF%0D%0A%2388A649%0D%0A%23A6121F%0D%0A&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) to figure out which foreground colours passed WCAG contrast regulations. Most of the colours were absolutely not compatible with each other, so I added #FFFFFF Black and #000000 White, which worked well with each of the various colours as shown on the grid below. With the palette being composed of primary and secondary colours, there weren’t too many options for some of the colours extracted for the theme.  
![EightShapes Contrast Grid](../duality/docs/screenshots/contrast-grid.png)

### *Imagery*
* Hero Image  
The Hero image was sourced on [freepik.com](www.freepik.com) and was generated by their Ai. Its name was 'Illustrated rendering of twin avatar' and it came up in search results for the term 'Duality'.
![Original Duality image](../duality/docs/screenshots/original-duality.png)  
The image depicts good and evil, dark and light, but the colours weren't quite right. I used [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) to change up the image so the colours matched traditional comic book primary and secondary colour schemes. This gave a clearer indication of good and evil.
![Final Duality Image](../duality/docs/screenshots/hero-image.avif)

* Logo
I originally chose a Yin Yang symbole for the logo because of its connotations of Duality, but it didn't really fit. So I searched on Adobe Stock for imagery representing duality/infinity/masks, and found this particular emblem:  
![Infinity flame icon](../duality/docs/screenshots/original-logo.png)  
The colours weren't quite right so again, I used Adobe Photoshop to change it up:  
![Final Duality Logo](../duality/docs/screenshots/logo.avif)

### *Typography*

* **Racing Sans One (Decorative) - logo/title.** High contrast Sans Serif font, designed for large headlines and titles. Features sharp angles and streamlined curves to convey a sense of motion and energy.  

* **Prompt (Structured) - headings in italic.** Highly legible Sans Serif geometric font, designed for performance on tech interfaces. Clean and contemporary. 

* **Inder (Easy Reading) - body text.** Low contrast sans serif, can be used on a wide range of screen sizes. Clean lines and absence of decorative elements means it’s perfect for smaller text on Legend cards. 
![Font Pairing](../duality/docs/screenshots/font-pairing.png)

### *Wireframes*
Wireframes were produced using [Bootstrap Studio](https://bootstrapstudio.io/), which has the added bonus of generating a skeletal HTML framework for my pages that can then be further customised with my own CSS styling and animations. Bootstrap Studio is worth every penny -  I was lucky enough to use it for free during my course, but would absolutely pay for the full version in the future.

Bootstrap Studio let me quickly build my design for scaling across different viewports, too.

The published version of the wireframe template can be found here:  
[Duality Wireframe Published](https://billowing-mountain-0627.bss.design/index.html)



### *End Product Design Changes*
The only changes made were to the layout created by Bootstrap Studio in places. Having the info cards on the main page only slightly covering the hero image looked unfinished in reality, so I had the hero image cover the whole page and added a glassmorphic effect to the cards. I also had to tweak a bit more using flex properties to get the cards to sit in the correct place. 

I added filters to the shop and the binder pages

Everything else stayed pretty much the same - I hadn't added styling to the wireframes this time, I just used them to mockup a skeletal layout for each page.

## **Features**

### *Users*

### *Characters*
The characters were extracted from a JSON file provided by a [github hosted superhero-api file](https://akabab.github.io/superhero-api/api/all.json) based on [superheroapi.com](https://superheroapi.com/). Their IDs ranged from 1-731, but there were only 563 characters in the file in total. I decided to keep the characters in the JSON file within the project and only store unique key data in the CHARACTER_CARD model, such as ID, name, rotation status, as well as foreign keys to other data models, such as rarity and archetype. This kept the data clean and following best practice in regards to relational databases.

Using ChatGPT and Gemini, we created mapping logic to assign one of the 12 Hero's Journey archetypes to every character in the file. 

#### **Archetype Mapping Logic**

This map classifies characters based on a priority system that favors established narrative roles and keywords over raw power statistics.

| \# | Archetype | Alignment | Quantitative Criteria | Core Narrative Role | Shadow Side |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **1** | **Hero** 🦸‍♂️ | Good | **P \>= 90 or C \>= 90** (or heroic occupation override) | The protagonist; figure of **ultimate power** and moral virtue. | Arrogance, debilitating savior complex. |
| **2** | **Destroyer** 💥 | Bad | **P \>= 75 or C \>= 75** (or 'tyrant' keyword override) | The primary antagonist defined by **overwhelming physical force** and annihilation. | Mindless violence, self-destruction. |
| **3** | **Shadow** ⚔️ | Bad | **I \>= 70** (or 'mastermind' keyword override) | The **cunning, intellectual villain**; the strategist and manipulator behind the scenes. | Isolation, paranoia, underestimating simplicity. |
| **4** | **Mentor** 🧙‍♀️ | Good | **I \>= 70 and P 40–74** (or 'professor' keyword override) | The **wise guide** who provides wisdom and strategy; non-combative support. | Manipulative teacher, paralyzing fear of direct action. |
| **5** | **Ally** 🤝 | Good | **P 40–74** (or 'sidekick' keyword override) | The **loyal companion** providing reliable skills and essential emotional grounding. | Overdependence, jealousy toward the Hero. |
| **6** | **Innocent / Warrior** 🛡️ | Good | **75 \<= P/C \< 90** (or 'lieutenant' keyword override) | A **powerful, specialized soldier** or high-power sidekick; secondary combat asset. | Over-reliance on violence, used as an expendable asset. |
| **7** | **Threshold Guardian** ⚖️ | Neutral | **P 40–70 and I 40–74** (or 'guard' keyword override) | A morally ambiguous figure who **tests the hero’s resolve** before a major transition. | Petty obstructionism, gatekeeping. |
| **8** | **Trickster** 🦊 | Bad/Neutral | **P 40–74 \+ High Speed** (or 'jester' keyword override) | The **chaos agent**; a disruptive figure using speed, deception, and mischief to challenge order. | Destructive chaos, deceit for selfish gain. |
| **9** | **Shapeshifter** 💋 | Any | **Override P1:** Name/Occupation keywords | The **elusive figure** whose primary power is changing form, creating tension and doubt. | Betrayal, identity loss, moral duplicity. |
| **10** | **Temptress** 💃 | Any | **Override P2:** Occupation keywords | The **seductress or enchanter** who poses a dangerous distraction to the hero. | Obsession, weaponized desire. |
| **11** | **Creator** 💡 | Neutral | **I \>= 70 and P 40–70** (or 'inventor' keyword override) | The **intellectual neutral force**; the inventor or builder who controls technology and discovery. | Losing control of inventions, moral ambiguity. |
| **12** | **Herald** 🕊️ | Good | **P \< 40 and I 40–74** (or 'messenger' keyword override) | The **messenger** who delivers the call to adventure or initiates the journey. | False prophecy, inability to act. |
| **13** | **Innocent** 👶 | Good/Neutral | **P \< 30 and I \< 40** (or 'civilian' keyword override) | The **moral compass** or vulnerable figure who symbolizes hope and needs protection. | Denial, self-destruction. |

#### **Quantitative Criteria Key**

This table defines the abbreviations used in the **Quantitative Criteria** column of the Archetype Model Reference. These values correspond directly to the character's **Powerstats** data.

| Abbreviation | Full Stat Name | Definition |
| :---- | :---- | :---- |
| **P** | **Power** | A character's potential for destructive force, energy projection, or non-physical abilities. |
| **C** | **Combat** | A character's effectiveness in unarmed fighting; their training and skill in battle. |
| **I** | **Intelligence** | A character's mental capacity, strategic skill, planning ability, and knowledge. |
| **S** | **Speed** | How fast a character can move, react, and process information. |

#### **Interpretation Notes**

* **P/C**: Used in the Innocent / Warrior criteria (75 \<= P/C \< 90\) and means either the Power **or** Combat stat meets the criteria.  
* **Numeric Ranges**: All quantitative rules use a 0-100 scale, where **90-100** is considered *Ultimate*, **75-89** is *High*, and **40-74** is *Moderate*.


### *Cards*
Cards have been designed using Bootstrap 5.3 card components, and customised with CSS3 styling and animations. They are responsive across screen sizes and their layout reflows as the screen changes. All cards show their publisher/universe, the character name and their total stats rarity.
They have a glassmorphic effect with border shadow for a lifted 3D effect, and glow around the edges on hover. 

On the shop, cards scale up on hover.  
![Shop card](../duality/docs/screenshots/shop-card.jpg)
![Shop card hover effect](../duality/docs/screenshots/shop-card-hover.jpg)

In the binder, cards flip on hover for additional content.  
![Binder card](../duality/docs/screenshots/binder-card.jpg)
![Binder card hover effect](../duality/docs/screenshots/binder-card-hover.jpg)

### *Responsiveness*
Duality: Legends Unchained has been designed mobile-first, built initially to look good on a screen 320px wide in Google Chrome. It is responsive across various screens and devices up to 4k (2560+). This has been achieved using Bootstrap grid sizes as well as CSS3 media queries to ensure the layout changes appropriately and looks good across all screen sizes. 

### *Header*
The header features a navbar whose nav-items arestyled with a skewed effect for a dynamic feel. The nav-items glow on hover, and keep the glow and a changed colour when active. The navbar will automatically distribute space evenly across nav-items to keep a consistently spaced feel.  
![Header with nav items and nav-brand](../duality/docs/screenshots/header.jpg)

On mobile and tablet screens, the navbar collapses and is replaced with a burger icon. A dropdown of nav items appears that keeps all the same hover and active effects.
![Header on mobile with collapsible navbar](../duality/docs/screenshots/header-mobile.jpg)


The nav-brand consists of a customised logo and the app name in gradient colours ([see Design section](#design)).  
![Navbrand with logo and title text.](../duality/docs/screenshots/navbrand.jpg)

The header is always fixed to the top so that navigation is easy to find and use.

### *Footer*
The footer features a copyright notice, a socials icon area and shows whether a user is signed in or out. The footer is fixed on screens 768px and up, but not on mobile to make more room for the content.  
![Footer](../duality/docs/screenshots/footer.jpg)

The socials icons feature a link to my personal Facebook page, my LinkedIn account and my Github. The icons change colour and glow on hover.  
![Socials icons hover effect](../duality/docs/screenshots/socials-hover.jpg)

The login status area will display a user's display name, if they have one, their username if they don't and will show you are not currently logged in if you haven't signed in, or if you signed out.  
![Login status area](../duality/docs/screenshots/login-status.jpg)


### *Home Page*
The home page features a customised image that is strategically placed to best effect on small and large screens.

Three hero cards explain what the app is about, with links to the shop and a user's binder. This text changes depending on a user's login status, directing them to register/sign in instead.  
![Home page on a larger screen](../duality/docs/screenshots/hero-section-lg.jpg)

The hero cards change to a carousel on small screens that cycles through automatically - this was designed to keep the home page compact and prevent an overly long screen to scroll vertically down.  
![Home page on a mobile screen](../duality/docs/screenshots/hero-section-mobile.jpg)

### *Shop Page*
The shop features a distinct title area and contains a grid of cards pulled through from the latest shop schedule items.
The layout of card grid responsively reflows on different screen sizes and the cards themselves also responsively change size.  
![Shop page](../duality/docs/screenshots/shop.jpg)

The shop features filters:
* Rarity, which always shows all rarities available in the rarity table
* Alignment, which shows only the alignments currently available in the shop
* Universe, which again shows only the universes/publishers currently available in the shop.  
![Shop filters](../duality/docs/screenshots/filters.jpg)

The filters can be used in conjunction with each other and set back to 'All'.
The filters are styled with a glassmorphic effect and have the same hover effect as the nav-items. The options list is also styled to match the app's colour scheme.  
![Shop filters](../duality/docs/screenshots/filter-hover.jpg)  
![Shop filters](../duality/docs/screenshots/filter-options.jpg)

The cards in the shop are generated by scheduled items attached to a shop scheduler. If a shop schedule doesn't already exist, one will be created when the shop is visited. 12 random characters will be added to the schedule and will populate the shop in order of highest rarity first. 

Each character card generated from this schedule features a buy button, which populates with the price of the card based on its rarity. The buttons will only display for logged-in users, so guests can browse the shop but have to sign up to purchase anything.
If a user already owns a card, a disabled button in a different colour will display instead.  
![Card that is already owned](../duality/docs/screenshots/card-owned.jpg)  
![Card with buy button](../duality/docs/screenshots/card-price.jpg)
![Card displayed for guest](../duality/docs/screenshots/shop-card.jpg)

Clicking 'Buy Now' will take the user to a confirmation page, where they have the option to either continue with their purchase, or cancel it completely before hitting the Stripe system.
![Confirmation of purchase page](../duality/docs/screenshots/continue%20purchase.jpg)

If the user continues with their purchase, the name of the character, their image and the price of the card will be sent through to the Stripe checkout page.  
![Stripe character card details](../duality/docs/screenshots/stripe-card.jpg)

Depending on if the purchase fails, is cancelled, or is successful, one of three templates will load:
* cancel.html gives a button to go back to the shop
* error.html passes the failure error as a string and gives a button to go back to the shop
* success.html gives the transaction details and a button to go to the binder

Note: Logic has been built into the system so if two users happen to access the shop at the same time, and there is no current schedule, it won't crash trying to create two schedules when there can only be one. Instead, it will allow a schedule to be created and will retry fetching that schedule for the other request.

### *Binder Page*
The binder page features filters, much the same as the shop page - by Rarity, Alignment and Universe. As per the [Card Features](#cards) section, the cards also flip on hover to provide extended information about each character.

### *Profile Page*
The profile page features a disabled version of the edit-profile form, with an edit button that takes the user to an editable version of the form which allows them to change their first name, last name, email address, and display name. Display name is stored on a custom model and made accessible through the User model via a shared property. The admin is customised so that the user profile information appears inline the User admin page and both can be edited at the same time.

![View profile page](../duality/docs/screenshots/view-profile.jpg)
![Edit profile page](../duality/docs/screenshots/edit-profile.jpg)





### Admin
* Shop Scheduler
* Schedule items - inline
* Customer User admin so that other model admins can be shown inline
* Inline usercards and inline userprofile
* CharacterCard additional actions for rotation - take out of rotation/put into rotation
* CharacterCard searchbar for characters by name
* Hook method for ScheduledItems, so the only items eligible to be allocated to a schedule are those where rotation equals true
* Autocomplete field on shop schedule items for quicker allocating
* Search bar on CharacterCard model for quicker editing
* Custom method to show characters allocated to a particular schedule as a comma separated list







## **Security Features**

### *Authentication & User Management*
- Django Allauth is used to handle user registration, login, logout, and account management.
- Provides built-in security features such as password hashing, session management, and optional email verification.
- Authentication logic is handled by Django’s proven authentication framework rather than custom code.

### *Access Control*
- Views and functionality are restricted based on authentication status.
- Users must be logged in to access account-specific features such as profiles and purchases.
- Django’s built-in request user context is used to ensure users can only access their own data.

### *Permissions & Roles*
- Administrative actions are restricted to staff and superuser accounts via Django’s admin permissions.
- Standard users do not have access to admin-only functionality.
- Role separation ensures that sensitive management actions cannot be performed by regular users.

### *Environment Variables*
- Sensitive configuration data is stored in an `env.py` file, which is excluded from version control via `.gitignore`.
- Environment variables include:
  - `SECRET_KEY` (Django project key)
  - `DATABASE_URL` (PostgreSQL database connection)
  - `CLOUDINARY_URL` (media storage)
  - `STRIPE_SECRET_KEY` (payment processing)
- The virtual environment (`.venv`) is also excluded from GitHub to prevent exposure of system-specific files and dependencies.

### *Deployment Security*
- `DEBUG` mode is disabled in production to prevent sensitive error information being exposed.
- No passwords, API keys, or secrets are committed to the repository.
- Production environment variables are managed securely using Heroku Config Vars.

### *Payment Security*
- All payment processing is handled by Stripe, a PCI-DSS compliant payment provider.
- The application never stores, processes, or transmits card details.
- Stripe API keys are stored securely using environment variables.
- The application only receives non-sensitive payment information such as transaction identifiers and payment status.


## **Future Features**
* Ability to trade cards  
* 1v1 card battles  
* Audio effects
* A fancier binder
* Search function on the Binder
* Pagination for the Binder
* Sort function on the Binder so it can be sorted by most recent purchase
* Ability to search by rarity/universe/alignment/archetype on the shop schedule items admin to allow 'type' shops. IE a Marvel only set of characters.
* Change the shop scheduler so that instead of creating a new schedule on a visit, it is an automated task every 24 hours.
* A timer countdown for the shop, so customers can see when the current batch of characters will be replaced.
* Fancy website colour changes relating directly to how many cards a user has that are one alignment or another.



## **Models and Data Relationships**
### *Entity Relationship Diagram*
This Entity Relationship Diagram for Duality was created using [Mermaid](https://mermaid.js.org/)’s built-in ERD diagramming tool. [ChatGPT](https://openai.com/index/chatgpt/) was used to double check my logic.

### *Overview*
This section contains the Django models for the Duality LC application, a card-collecting platform where collectors can purchase Legends cards and store them in an online binder.

Models include:
* **CharacterCard**: Stores the base Legends stored in the system and their basic information - extended data is kept in a JSON file(legends.json)
* **Archetype**: Represents literary archetypes for characters based on the Hero's Journey concept. This allows characters to be categorised narratively (e.g., "The Hero," or "The Shadow") and stores traits for each archetype.
* **Rarity**: Determines the rarity of character cards and sets a price accordingly. Has a numeric level field for algorithmic calculations and ordering.
* **ShopScheduler**: Represents a timed shop rotation. Each scheduler must have one or more shop schedule items defining which characters appear and their rotation-specific sale prices. A custom function defines the schedule end time as now + 24 hours. 
* **ShopScheduleItems**: Acts as a join table linking ShopScheduler and CharacterCard.  
Each row = one character in one rotation.  
Supports assigning any subset of characters to any rotation independently.  
Enables per-rotation pricing or other metadata without affecting the base character record.
* **UserCards** Stores details of the character cards that a user has purchased, including the date and time it was bought, and the purchase price at the time.
* **UserProfile** Stores extended user details such as display name.

### *Model Relationships (ERD Notation)*

**USER ||--|| USER_PROFILE : "purchases"**  
* Each user has exactly one profile.  
* USER_PROFILE stores extended info like display name, while the base USER holds login credentials and name.

---

**USER ||--o{ USER_CARDS : "purchases"**  
* Each user can purchase zero or more user_cards.  
* User cards belong to exactly one user.  
* UserCards store purchase details such as which character was bought, the price paid, and the date of purchase, while the base USER holds login credentials and email address.

---

**USER_CARDS }o--|| CHARACTER_CARD : "is based on"**  
* Each UserCard is based on exactly one character.  
* A character card can have zero or more user cards associated with it.  
* This links a purchased card to a specific character, capturing its stats, rarity, archetype and other metadata.

---

**CHARACTER_CARD }|--|| ARCHETYPE : "belongs to"**  
* Each character belongs to exactly one archetype.  
* An Archetype is assigned to one or more characters.  
* A character must have an archetype.  
* Archetypes store literary classifications (like “The Hero” or “The Shadow”) and traditional archetype traits for that classification. 
* CHARACTER_CARD stores global availability for shop rotations and links to the archetype and rarity tables.

---

**CHARACTER_CARD }|--|| RARITY : "has"**  
* Each character is assigned exactly one rarity.  
* Rarity is assigned to one or more character cards.  
* Character cards must have a rarity.  
* RARITY defines the classification (Common, Uncommon, Rare, Epic, Legendary, Mythic), a numerical level, and a base price. This allows characters to be consistently valued and ordered in the shop.

---

**SHOP_SCHEDULER ||--|{ SHOP_SCHEDULE_ITEMS : "has"**  
* A shop scheduler must include one or more schedule items.  
* One or more shop schedule items belong to a shop scheduler.  
* A shop scheduler must have at least one schedule item.  
* Stores per-rotation metadata, such as sale prices.

---

**CHARACTER_CARD 0{--||SHOP_SCHEDULE_ITEMS "appears in"**  
* Each character card can appear in zero or more schedule items.  
* Each schedule items corresponds to exactly one character. 
* Characters can appear multiple times over time, but only once per shop scheduler. 
* Also tracks rotation-specific details like sale price.

---
### *Model Fields*

**USER**
| Column Name    | Type     | Constraints / Notes                                       |
| -------------- | -------- | ----------------------------------------------------------|
| id             | int      | PK                                                        |
| username       | string   | CharField:unique                                          |
| email          | string   | EmailField:EmailValidator                                 |
| password       | string   | CharField                                                 |

---

**USER_PROFILE**
| Column Name    | Type     | Constraints / Notes                                         |
| -------------- | -------- | ------------------------------------------------------------|
| id             | int      | PK                                                          |
| user_id        | int      | FK to User. CharField, OneToOne: USER.id, on_delete=CASCADE |
| display_name   | string   | CharField, max_length=300                                   |

---

**USER_CARDS**
| Column Name    | Type     | Constraints / Notes                                       |
| -------------- | -------- | ----------------------------------------------------------|
| id             | int      | PK                                                        |
| stripe_id      | string   | CharField, max_length=300                                 |
| order_reference| string   | CharField, max_length=300                                 |
| owner          | int      | FK → `USER.id`, on_delete=SET_NULL, null=True, blank=True |
| character      | int      | FK → `CHARACTER_CARD.id`, on_delete=PROTECT               |
| date_purchased | datetime | DateTimeField(auto_now_add=True)                          |
| purchase_price | decimal  | DecimalField                                              |

---

**ARCHETYPE**
| Column Name        | Type   | Constraints / Notes |
| ------------------ | ------ | ------------------- |
| id                 | int    | PK                  |
| literary_archetype | string | CharField           |
| archetype_traits   | string | TextField           |

---

**RARITY**
| Column Name | Type    | Constraints / Notes                                                       |
| ----------- | ------- | ------------------------------------------------------------------------- |
| id          | int     | PK                                                                        |
| name        | string  | CharField (Common, Uncommon, Rare, Epic, Legendary, Mythic) Unique = True |
| level       | int     | PositiveIntegerField (0-5), Unique=True                                   |
| price       | decimal | DecimalField, NULL=False                                                  |

---

**SHOP_SCHEDULER**
| Column Name   | Type     | Constraints / Notes                     |
| ------------- | -------- | ----------------------------------------|
| id            | int      | PK                                      |
| start_time    | datetime | DateTimeField, auto_now_add=True        |
| end_time      | datetime | DateTimeField, default=default_end_time |
| rotation_type | string   | CharField                               |


---

**SHOP_SCHEDULE_ITEMS**
| Column Name       | Type    | Constraints / Notes                 |
| ----------------- | ------- | ------------------------------------|
| id                | int     | PK                                  |
| shop_scheduler_id | int     | FK → `SHOP_SCHEDULER.id`            |
| character_id      | int     | FK → `CHARACTER_CARD.id`            |
| sale_price        | decimal | DecimalField, NULL=True, BLANK=True |

---

**CHARACTER_CARD**
| Column Name                 | Type    | Constraints / Notes                                |
| --------------------------- | ------- | -------------------------------------------------- |
| id                          | int     | PK                                                 |
| name                        | string  | CharField                                          |
| can_participate_in_rotation | boolean | default=True                                       |
| archetype                   | int     | FK → `ARCHETYPE.id`, on_delete=PROTECT             |
| rarity                      | int     | FK → `RARITY.id`, on_delete=PROTECT, NULL=False    |

## **Testing**

### *User Story Testing*

### *Automated Testing*

#### **The W3C Markup Validation Service**

#### **The W3C CSS Validation Service**

#### **The JSHint Validation Service**

#### [**CI Python Linter**](https://pep8ci.herokuapp.com/)
* **Core App**
    * fix_legend_id.py - all clear, no errors found
    * import.py - all clear, no errors found
    * rarity-calculation.py - all clear, no errors found
    * rarity-update.py - all clear, no errors found
    * datastore.py - all clear, no errors found
    * admin.py - all clear, no errors found
    * apps.py - all clear, no errors found
    * models.py - all clear, no errors found
    * tests.py - all clear no errors found
    * urls.py - all clear, no errors found
    * views.py - all clear, no errors found
* **Shop App**
    * admin.py - all clear, no errors found
    * apps.py - all clear, no errors found
    * models.py - all clear, no errors found
    * tests.py - all clear, no errors found
    * urls.py - all clear, no errors found
    * views.py - all clear, no errors found
* **Binder App**
    * models.py - all clear, no errors found
    * views.py - all clear, no errors found
    * urls.py - all clear, no errors found
    * admin.py - all clear, no errors found
* **Root Directory Files**

#### [**JSONLint**](https://jsonlint.com/)
* legends.json file is valid.
* archetypes.json file is valid
* charactercard_with_legend_id is valid
* charactercard.json is valid
* rarity.json is valid

#### **The WAVE Webb Accessibility Evaluation Tool**
* Home Page - no errors  
![Alt text](../duality/docs/testing/wave-home.png)

* Shop Page - no errors  
![Alt text](../duality/docs/testing/wave-shop.png)

* Binder Page - no errors  
![Alt text](../duality/docs/testing/wave-binder.png)

* Register Page - no errors  
![Alt text](../duality/docs/testing/wave-register.png)

* Login Page - no errors  
![Alt text](../duality/docs/testing/wave-login.png)

* Logout Page - no errors  
![Alt text](../duality/docs/testing/wave-logout.png)

#### **Chrome Lighthouse**
* Home Page(mobile)  
![Alt text](../duality/docs/testing/homepage-lighthouse-mobile.png)

* Home Page(desktop)  
![Alt text](../duality/docs/testing/homepage-lighthouse-desktop.png)

* Shop Page(mobile)  
![Alt text](../duality/docs/testing/shop-lighthouse-mobile.png)

* Shop Page(desktop)  
![Alt text](../duality/docs/testing/shop-lighthouse-desktop.png)



### **Manual Testing**

Mobile 320px
Chrome



Mobile 320px. Tablet 768px. Laptop 1024px. Laptop L 1440px. 4k 2560px.

All nav links work on all pages
All external links open in a new browser window
The layout reflows and changes as expected across different screen sizes
The background image appears and disappears as it should on different screen sizes
The logo text always links back to the home page from every other page
Hover colours work as expected on laptops and desktops
All required form fields have to be filled in
The burger icon expands and collapses the nav list as expected on mobile screens. If left open, it will disappear by itself when navigating to another page.


Edge
Mobile 320px. Tablet 768px. Laptop 1024px. Laptop L 1440px. 4k 2560px.

All nav and footer links work on all pages
All external links open in a new browser window
The layout reflows and changes as expected across different screen sizes
The background image appears and disappears as it should on different screen sizes
The logo text always links back to the home page from every other page
Hover colours work as expected on laptops and desktops
All required form fields have to be filled in
The burger icon expands and collapses the nav list as expected on mobile screens. If left open, it will disappear by itself when navigating to another page.
FireFox
Mobile 320px. Tablet 768px. Laptop 1024px. Laptop L 1440px. 4k 2560px.

All nav and footer links work on all pages
All external links open in a new browser window
The layout reflows and changes as expected across different screen sizes
The background image appears and disappears as it should on different screen sizes
The logo text always links back to the home page from every other page
Hover colours work as expected on laptops and desktops
All required form fields have to be filled in
The burger icon expands and collapses the nav list as expected on mobile screens. If left open, it will disappear by itself when navigating to another page.


Safari
Tested on an iPhone SE 2023

The burger nav dropdown works as expected on all pages, expanding, collapsing and disappearing as it should
All nav links work on all pages
All external links open in a new browser window
All active nav-links display in the appropriate colour on the appropriate page
All required form fields have to be filled in
The logo text takes you back to the home page from every page


* Tested characters imported safely after running import.py and that archetypes were allocated to all characters - checked via Django admin. Exception errors raise if the file doesn't exist at the specified path, if the JSON data is malformed, or if the OS denies permissions. Exception errors also raise if invalid values or if bad values violate database rules.
* Tested that rarities were assigned to all characters after running rarity-update.py - checked via Django admin. Built-in logic to compare id and name from the JSON file, to id and name in the CharacterCard model table. Exception errors raise if the CharacterCard doesn't exist, and any characters not allocated a rarity will print to the terminal.
* Checked that the method of grabbing the json data for each character returns the correct details by manually comparing characters to the json file
* Checked that UserCards showed inline to Users in the Admin panel after deregistering the User admin and creating a custome one.
* Checked that ShopScheduleItems show inline to Shop Scheduler after creating an inline admin class
* Checked that ShopSchedulers show a comma separated list of characters allocated to the schedule
* Checked that the autocomplete works when creating shop schedule items via Admin
* Checked that the search function works on the CharacterCard admin
* Checked that only characters where rotation = True show as eligible to become Shop Schedule Items
* Checked that the logic works in the view to remove any characters where initally rotation was true, but that became false after the item was already displaying in the shop
* Checked that the Shop filters work solo and in tandem with each other to show the correct characters
* Checked that multiple Shop Schedulers with crossover dates showed all items on all schedulers
* Checked that when there were no currently active schedules, a new one was created when visiting the shop
* Checked that the shop still created a schedule properly after adding a try/except block to the class method that is called in the view to create it



### **Unit Testing**

The project includes comprehensive unit tests for models and views using Django's `TestCase`. Key areas covered:

#### Core Template & View Tests
- Confirms that the home page (`index`) loads successfully.
- Checks that the correct template (`core/index.html`) is used.
- Verifies page content rendering.

#### CharacterCard Model Tests
- Ensures `CharacterCard` verbose names (singular/plural) are correct.
- Validates character creation and attributes (name, rotation eligibility).
- Confirms correct association with `Archetype` and `Rarity`.
- Checks character ordering and string representation.

#### Rarity Model Tests
- Validates rarity attributes: name, level, price.
- Checks verbose names (singular/plural) and ordering.
- Confirms string representation returns the rarity name.

#### Archetype Model Tests
- Ensures archetype attributes (name, traits) are correct.
- Checks verbose names (singular/plural) and ordering.
- Confirms string representation returns the archetype name.


## **Technology Used**

* [Adobe Color](https://color.adobe.com/)  
* [Adobe Fonts](https://fonts.adobe.com/)  
* [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)  
* [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/download/)  
* [Bootstrap Studio](https://bootstrapstudio.io/)  
* [Canva](https://www.canva.com/en_gb/)  
* [Cloudinary](https://cloudinary.com/)  
* [CSS3](https://www.css3.info/)
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/)  
* [DJ-database-url](https://pypi.org/project/dj-database-url/)  
* [Django 5.2.7](https://www.djangoproject.com/)  
* [Django allauth](https://docs.allauth.org/)  
* [Github](https://github.com/)
* [Github Desktop](https://desktop.github.com/download/)
* [Google Docs](https://docs.google.com/)  
* [Google Drive](https://drive.google.com/drive/quota)  
* [Google Fonts](https://fonts.google.com/)  
* [Gunicorn](https://gunicorn.org/)  
* [HTML5](https://www.w3schools.com/html/)
* [Javascript](https://www.w3schools.com/js/)  
* [Mermaid](https://mermaid.js.org/)   
* [Psycopg2](https://pypi.org/project/psycopg2/)  
* [Python 3.13](https://www.python.org/)
* [Stripe](https://stripe.com/gb)
* [Superhero API](https://www.superheroapi.com/)  
* [Visual Studio Code](https://code.visualstudio.com/)  
* [Whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html)

## **Coding Help**

* [Django Docs](https://www.djangoproject.com/)  
* [W3Schools](https://www.w3schools.com/)  
* Badges on images in Bootstrap - [stackoverflow](https://stackoverflow.com/questions/32815975/how-to-place-a-badge-in-lower-right-corner-of-an-img-in-bootstrap)
* Working with JSON Data in Python 
    * [realpython.com](https://realpython.com/python-json/)
    * [geeksforgeeks](https://www.geeksforgeeks.org/python/json-loads-in-python/)
    * [stackoverflow](https://stackoverflow.com/questions/20199126/reading-json-from-a-file)
    * [hackernoon](https://hackernoon.com/how-to-read-and-write-json-files-in-python)
* Help generating random choices from a list of objects
    * [geeksforgeeks](https://www.geeksforgeeks.org/python/python-select-random-value-from-a-list/)
    * [W3 Schools](https://www.w3schools.com/python/ref_random_choices.asp)
* Help understanding how to write a custom management command for importing json data into a model table:
    * [geeksforgeeks - how to import json to django model](https://www.geeksforgeeks.org/python/how-to-import-a-json-file-to-a-django-model/)
    * [codementor - data import from json](https://www.codementor.io/@happinessnwosuc/data-import-from-url-local-csv-and-json-files-into-db-django-app-d9z43iqbx)
    * [geeksforgeeks - custom management commands](https://www.geeksforgeeks.org/python/custom-django-management-commands/)
* Help understanding pathlib.Path - [geeksforgeeks](https://www.geeksforgeeks.org/python/get-parent-of-current-directory-using-python/)
* Handle() method typeError - [stackoverflow](https://stackoverflow.com/questions/41401202/django-command-throws-typeerror-handle-got-an-unexpected-keyword-argument)
* Help with filtering out a particular record in order to update it - [stackoverflow](https://stackoverflow.com/questions/2712682/how-to-select-a-record-and-update-it-with-a-single-queryset-in-django)
* Help with creating shapes in CSS - [css-tricks.com](https://css-tricks.com/the-shapes-of-css/)
* Help with CSS gradient text [cssgradient.io](https://cssgradient.io/blog/css-gradient-text/)
* Help with Django inline admin - [medium.com](https://medium.com/django-unleashed/mastering-django-inline-admin-tabularinline-and-stackedinline-examples-c9f17accde84)
* Help with customising ForeignKey choices in Django Admin - [foysalff.medium.com](https://foysalff.medium.com/customizing-foreignkey-choices-in-django-admin-tailoring-forms-based-on-user-roles-2f6245b18c6d)
* Help with generator expressions instead of looping through a whole file - [geeksforgeeks](https://www.geeksforgeeks.org/python/python-find-dictionary-matching-value-in-list/)
* Help understanding class methods and static methods [djangocentral.com](https://djangocentral.com/classmethod-and-staticmethod-explained/)
* Help sorting with lambda in Python [stackoverflow.com](https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python)
* Help creating a constraint on the UserCards model to prevent owners having more than one Usercard for the same Character - [forum.djangoprojects.com](https://forum.djangoproject.com/t/how-to-make-a-django-uniqueconstraint-that-checks-fields-in-a-position-independant-way/19062)
* Help rendering two models in one form - [forums.djangoprojects.com](https://forum.djangoproject.com/t/create-a-form-using-two-models/21234/5)
* Help rendering form fields, while using crispy forms, as readonly. Decided not to use this method ultimately, created the form with disabled fields insteads in the view - [stackoverflow](https://stackoverflow.com/questions/21559380/django-crispy-forms-readonly)



## **Interesting Bugs**
* The API I wanted to use came with a json file that would allow me to import the characters directly into the database, however there was a lot of extended information that didn't make sense to store in the database without breaching Database Normalisation. I ended up creating a basic CharacterCard model and then stored the json file in a data folder for the app to open and use the extended data.
* Not a bug, but something I found interesting to accomplish - creating management commands
    1. **import.py** to help with my JSON data import into the CharacterCard model, and assign archetypes from the Archetype model using a map of archetypes and their IDs, when the JSON data only had a string value for archetype.
    2. **rarity_calculation** to access power stat data from inside nested dictionaries, total it up for each character and put it in a sorted list so I could figure out the range to define rarities in the Rarity model.
    3. **rarity_update** to iterate through the json file, grab the id and name of each character, use the id to grab the same character from the CharacterCard model and perform a check to see if the name matches. If so, it assigned a rarity to that character based on the sum of the character's power stats against a predefined range.
    4. **fix_legend_id** to open the dumped data for the CharacterCard model, iterate through the file and for each item, grab the pk and create a legend_id field that matches the pk number, then output to a new fixture file. I was then able to flush the database and reimport from fixtures.
* Not a bug per se, but originally I had the home view opening up the legends json file at every request, in order to iterate through it and match up with the randomly generated sample of characters from the Charactercard model. This is okay with a small amount of data for a course project, but in actual fact its not very efficent or scalable. I used various resources (Django documentation and ChatGPT) to create a ready method in AppConfig to load up the data once at startup and store it in a global variable in my project's data folder. I then removed the file opening from the home view and iterated through the data stored in the global variable instead.
* The earlier import of json data into the CharacterCard model meant I had to create a custom pk for the model that wouldn't auto-increment, as I needed to manually assign IDs that already existed in the JSON dictionaries for each character. A  test later on reminded me that Django would no longer auto-assign and increment IDs to any future characters added to the app. This was sorted using the custom management command **fix_legend_id** to assign a separate integer field to legend_id that matches the current PK for each character, I was then able to change id to an AutoField.

## **Deployment**

### Creating a Github Fork
1. Navigate to the [repository](https://github.com/Nexiauk/Gameracy).
2. In the top-right corner of the page click on the down arrow next to the **Fork** button and select **Create a new fork**.
3. You can change the name of the fork in **Repository name** and add an optional description.
4. Tick **Copy the main branch only**.
5. Click the **Create a Fork** button.
6. A new repository should appear in your GitHub with the name you chose.

### Cloning a Github Repository
1. Navigate to the [repository](https://github.com/Nexiauk/Gameracy).
2. Click on the **Code** button on top of the repository and copy the link.
3. Open Git Bash and change the working directory to the location where you want the cloned directory.
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.

### Installing Requirements
1. Create a virtual environment in your local project folder.  
2. Activate the virtual environment.  
3. Install all required dependencies using the `requirements.txt` file using `pip install -r requirements.txt`  
4. Verify installation by running the project locally.  

### Preparing the Project
1. Ensure your Django project has a `requirements.txt` with all dependencies listed.  
2. Ensure your project has a `Procfile` at the root, specifying how Heroku should run the app.  
3. Make sure `ALLOWED_HOSTS` in `settings.py` includes your Heroku app domain.  
4. Ensure static files are configured for production (for example, using WhiteNoise).
5. Ensure `dj-database-url` is listed in `requirements.txt` so it is installed automatically.
6. Your `settings.py` should use `dj-database-url` to read the `DATABASE_URL` environment variable.  
  This ensures Django connects to the correct database in both local and Heroku environments.  
7. Set `DEBUG = False` in `settings.py` for production. 

### Creating an `env.py` File
1. In your local project directory, create a file named `env.py`.  
2. Add your sensitive environment variables to the file, for example:
   ```python
   import os

   os.environ['SECRET_KEY'] = 'your-secret-key'
   os.environ['CLOUDINARY_URL'] = 'your-cloudinary-url'
   os.environ['DATABASE_URL'] = 'your-local-database-url'
3. Ensure env.py is added to .gitignore so it is never pushed to GitHub


### Running Database Migrations and Collecting Static Files Locally
1. Check database migrations by executing `python manage.py makemigrations`.
2. Run database migrations locally to update the database schema by executing `python manage.py migrate`.
3. Collect static files locally so they are ready for deployment by executing `python manage.py collectstatic`.  
*Note: `DISABLE_COLLECTSTATIC=1` is needed to skip Heroku's automatic static collection when using Cloudinary.*

### Deploying Local Changes
1. Commit the changes using Git (`git add`, `git commit`).  
2. Push the changes to GitHub (`git push origin main`).  
3. Deploy the updated branch to Heroku using the steps in **Deploying on Heroku**.  

### Creating a Heroku App
1. Navigate to [Heroku](https://www.heroku.com/) and log in to your account.  
2. Click the **New** button in the top-right corner and select **Create new app**.  
3. Enter a unique name for your app.  
4. Select your preferred region.  
5. Click the **Create app** button to finalize the app creation.  
6. After the app is created, you will be taken to the app dashboard where you can configure settings and deploy your project.


### Configuring the App on Heroku
1. Navigate to the **Settings** tab of your app.  
2. Click **Reveal Config Vars**.  
3. Add the following variables:  
   - `CLOUDINARY_URL` → your Cloudinary account URL.  
   - `DISABLE_COLLECTSTATIC` → set to `1` if you want to skip automatic static collection.  
   - `DATABASE_URL` → automatically added if you enable Heroku Postgres (leave it as is).  
   - `SECRET_KEY` → your Django secret key.  
4. (Optional) Add any other third-party service keys your project needs

### Deploying on Heroku
1. Navigate to the **Deploy** tab of your Heroku app.  
2. Under **Deployment method**, select **GitHub**.  
3. Search for your GitHub repository and connect it.  
4. Under **Automatic deploys**, you can enable automatic deployment from the main branch if desired.  
5. Click **Deploy Branch** to deploy manually. 

### Verifying the Deployment
1. Click the **Open App** button in the top-right of the Heroku dashboard.  
2. Check that your Django project loads correctly in the browser.  
3. If any errors occur, click **More** → **View Logs** to troubleshoot.

### Optional Best Practices
- Keep all API keys and secrets in Config Vars, never in code.  
- Monitor logs regularly to catch any runtime errors.  
- Enable automatic deployment from GitHub for continuous updates.    

## **Credits**

### *Data*

* Data for 731 superheroes and villains - [SuperHeroAPI](https://www.superheroapi.com/)

### *Media*

* Media for 731 superheroes and villains - [SuperHeroAPI](https://www.superheroapi.com/)
* Socials icons for the Header/Footer - [Bootstrap Icons](https://icons.getbootstrap.com/)
* Hero image from [freepik.com](https://www.freepik.com/free-ai-image/illustrated-rendering-twin-avatar_94938018.htm#fromView=image_search&page=1&position=30&uuid=3f919ced-a2ab-4eae-9f4f-620c72eddb72&query=heroes+and+villains)
* Logo sourced from Adobe Stock images [stock.adobe.com](https://stock.adobe.com/uk/images/dynamic-flame-energy-abstract-icon-vibrant-abstract-emblem-featuring-a-central-blaze-embraced-by-flowing-red-and-blue-elements-symbolizing-balance-and-powerful-connection/1605298308?prev_url=detail)

### *Tools*
* Glassmorphism CSS generator - [css.glass](https://css.glass/)

### *Code*
* CSS Animation - The Pulse Effect [florin-pop.com](https://florin-pop.com/blog/2019/03/css-pulse-effect/)
* CSS Button Skew -  [codepen.io](https://codepen.io/dunyung1/pen/ZEGGWwB?editors=1100)

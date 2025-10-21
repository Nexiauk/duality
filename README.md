# Duality: Legends Unchained

[View the live project here](INSERT LINK HERE)

INSERT PICTURE HERE

This app has been created as a project during my [Code Institute](https://codeinstitute.net/) Level 5 Web App Development course.

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
Originally, I wanted to make a fairy-tale inspired card collection with characters and objects from classic stories. But when I started designing the cards, I realised the scope was bigger than I could handle. So I stepped back and looked for data sources that could bring a ready-made universe to life.  
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

* **Browse the available cards in the shop**, so that I can decide which ones to collect or purchase.

* **See at a glance which cards are free and which ones require payment**, so that I can make quick decisions on which cards to collect.

* **See at a glance the different card rarities and Universes**, so I can make informed collection decisions.

* **See at a glance the last time the shop refreshed**, so that I don’t waste time on a card stack I’ve already viewed.

* **See at a glance the next time the shop will refresh**, so that I know when to come back and check the shop again.

**Binder / Collection Management**

* **Add free cards to my binder with a single click**, so that I can build my collection quickly and efficiently.

* **Add purchasable cards to a basket with a single click**, so that I can efficiently purchase them if under time constraints.

* **See how many items are in my basket**, so that I can track my intended purchases.

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

* **Highlight special, featured, or new cards in the collection**, so I can encourage customer purchases and promotions.

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

The famous photograph “Lunch Atop Skyscraper” has a version that replaces the workers with Marvel and DC characters. I used [Adobe Color](https://color.adobe.com/) to generate a palette from a portion of that image where the colours are representative of old school comic hero and villain colours.  


#845ABF - Fuchsia Blue  
#AAB1BF - Eclectic  
#2182BF - Skylla  
#88A649 - Nasturtium Shoot  
#A6121F - Ecstatic Red

### *Colour Accessibility*
I used [Eight Shapes Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=%23845ABF%0D%0A%23AAB1BF%0D%0A%232182BF%0D%0A%2388A649%0D%0A%23A6121F%0D%0A&foreground-colors=%23000000%0D%0A%23ffffff%0D%0A%23AAB1BF%0D%0A%23845ABF%0D%0A%232182BF%0D%0A%2388A649%0D%0A%23A6121F%0D%0A&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp) to figure out which foreground colours passed WCAG contrast regulations. Most of the colours were absolutely not compatible with each other, so I added #FFFFFF Black and #000000 White, which worked well with each of the various colours as shown on the grid below. With the palette being composed of primary and secondary colours, there weren’t too many options for some of the colours extracted for the theme.  

### *Imagery*

### *Typography*

Avengeance - loved this for the title, but needed to pay for an annual subscription licence. Couldn’t justify the cost.  


#### **Final set**
* **Racing Sans One (Decorative) - logo/title.** High contrast Sans Serif font, designed for large headlines and titles. Features sharp angles and streamlined curves to convey a sense of motion and energy.  
* **Prompt (Structured) - headings in italic.** Highly legible Sans Serif geometric font, designed for performance on tech interfaces. Clean and contemporary.  
* **Inder (Easy Reading) - body text.** Low contrast sans serif, can be used on a wide range of screen sizes. Clean lines and absence of decorative elements means it’s perfect for smaller text on Legend cards. 

### *Wireframes*
Wireframes were produced using [Bootstrap Studio](https://bootstrapstudio.io/), which has the added bonus of generating a skeletal HTML framework for my pages that can then be further customised with my own CSS styling and animations. Bootstrap Studio is worth every penny \-  I was lucky enough to use it for free during my course, but would absolutely pay for the full version in the future.

### *End Product Design Changes*

## **Features**

### *Users*

### *Characters*
The characters were extracted from a JSON file provided by a [github hosted superhero-api file](https://akabab.github.io/superhero-api/api/all.json) based on [superheroapi.com](https://superheroapi.com/). Their IDs ranged from 1-731, but there were only 563 characters in the file in total. I decided to keep the characters in the JSON file within the project and only store uique key data in the CHARACTER_CARD model, such as ID, name, rotation status, as well as foreign keys to other data models, such as rarity and archetype. This kept the data clean and following best practice in regards to relational databases.

Using ChatGPT and Gemini, we created mapping logic to assign one of the 12 Hero's Journey archetypes to every character in the file. 

## Final Archetype Mapping Logic (Strict Shapeshifter Model)





### *Cards*
Cards have been designed using Bootstrap 5.3 card components, and customised with CSS3 styling and animations.

### *Responsiveness*
Duality: Legends Unchained has been designed mobile-first, built initially to look good on a screen 320px wide in Google Chrome. It is responsive across various screens and devices up to 4k (2560+). This has been achieved using Bootstrap grid sizes as well as CSS3 media queries to ensure the layout changes appropriately and looks good across all screen sizes. 

### *Header*

### *Footer*

### *Home Page*
Progress bar  
Dynamic background  
Hero section

### *Shop Page*
Add to basket  
Hover animations  
Shop countdown timer

### *Basket*
Remove from basket  
Proceed to payment  
Stripe Payment

### *Binder Page*
Filters  
Search  
Flippable cards  
Extra card content

### 

## **Security Features**

### *Authentication & User Management*
* Django Allauth is used to handle user registration, login, logout, and account management.  
* Provides built-in security features such as password hashing, email verification, and session handling.

### *Access Control*

### *Permissions & Roles*

### *Environment Variables*
* Sensitive data is stored securely in an env.py file, which is hidden via .gitignore.  
* Keys and settings stored in env.py include:  
* SECRET_KEY (Django project key)  
* DATABASE_URL (PostgreSQL database connection)  
* CLOUDINARY_URL (media storage)  
* .venv (virtual environment) is also excluded from GitHub, ensuring no dependencies or system files are exposed.

### *Deployment Security*
* DEBUG mode is disabled in production.  
* No passwords, API keys, or sensitive information are ever committed to the repository.  
* All environment-specific settings are managed securely via env.py.

### *Payment Security*

## **Future Features**
* Ability to trade cards  
* 1v1 card battles  
* Audio effects

## **Database Schema**
This Entity Relationship Diagram for Duality was created using [Mermaid](https://mermaid.js.org/)’s built-in ERD diagramming tool. [ChatGPT](https://openai.com/index/chatgpt/) was used to double check my logic.

### *Entity Relationship Diagram*

### *Models*

#### **USER Model**  
Stores login and display information for players.  

**Key fields:** 
* username (unique)
* email
* password

---

#### **USER_CARD Model**  
Represents a card purchased by a user. Each entry links a purchase to a specific character and records the price at the time of purchase.  

**Key fields:** 
* foreign keys to USER and CHARACTERS
* date purchased *
* price paid.  

---

#### **CHARACTER_CARD Model**  
Represents the base characters available in the system.  
**Key fields:**
* ID (PK)
* Name
* can_participate_in_rotation (boolean, default=True) - global eligibility for shop rotations
* Foreign keys to ARCHETYPE and RARITY - classify characters and determine rarity-based ordering or pricing  

Detailed attributes like powerstats, appearance, biography, work, connections, and images are stored in a JSON file.

---

#### **ARCHETYPE Model**  
Represents literary archetypes for characters. This allows characters to be categorized narratively (e.g., "The Hero," or "The Shadow").

**Key fields:** 
* literary archetype name
* archetype_traits.  

---

#### **SHOP_SCHEDULER Model**  
Represents a timed shop rotation. Each scheduler must have one or more SHOP_SCHEDULE_ITEMS defining which characters appear and their rotation-specific sale prices.

**Key fields:** 
* start_time
* end_time
* rotation_type

---

#### **SHOP_SCHEDULE_ITEMS Model**  
Acts as a join table linking SHOP_SCHEDULER and CHARACTER_CARD.  
Each row = one character in one rotation.  
Supports assigning any subset of characters to any rotation independently.  
Enables per-rotation pricing or other metadata without affecting the base character record.

**Key fields:** 
* foreign keys to SHOP_SCHEDULER and CHARACTER_CARD
* sale_price.

### *Model Fields*
```
erDiagram
    USER ||--o{ USER_CARDS : "purchases"
    USER_CARDS }o--|| CHARACTER_CARD : "is based on"
    CHARACTER_CARD }|--|| ARCHETYPE : "belongs to"
    CHARACTER_CARD }|--|| RARITY : "has"
    SHOP_SCHEDULER ||--|{ SHOP_SCHEDULE_ITEMS : "has"
    CHARACTER_CARD o{--|| SHOP_SCHEDULE_ITEMS : "appears in"

    USER {
        int id PK
        string username "CharField:unique"
        string email "EmailField:EmailValidator"
        string password "CharField"
        string display_name "CharField"
    }
    USER_CARDS {
        int id PK
        int user_id FK "References USER.id, on_delete=CASCADE"
        int character_id FK "References CHARACTER_CARD.id, on_delete=PROTECT"
        datetime date_purchased "DateTimeField(auto_now_add=True)"
        decimal purchase_price "DecimalField"
    }
    ARCHETYPE {
        int id PK
        string literary_archetype "CharField"
        string archetype_traits "TextField"
    }
    RARITY {
        int id PK
        string name "CharField (Common, Uncommon, Rare, Epic, Legendary, Mythic)"
        int level "PositiveIntegerField (0-5)"
        decimal price "DecimalField"
    }
    SHOP_SCHEDULER {
        int id PK
        datetime start_time "DateTimeField(auto_now_add=True)"
        datetime end_time "DateTimeField"
        string rotation_type "CharField"
    }
    SHOP_SCHEDULE_ITEMS {
        int id PK
        int shop_scheduler_id FK "References SHOP_SCHEDULER.id"
        int character_id FK "References CHARACTER_CARD.id"
        decimal sale_price "DecimalField"
    }
    CHARACTER_CARD {
        int id PK
        string name "CharField"
        boolean can_participate_in_rotation "default=True"
        int archetype FK "References ARCHETYPE.id, on_delete=PROTECT"
        int rarity FK "References RARITY.id, on_delete=PROTECT"
    } 
```

### *Model Relationship Declaration*
---
**USER ||--o{ USER_CARD : "purchases"**
Each user can purchase zero or more user_cards. 
User cards belong to exactly one user.
UserCards store purchase details such as which character was bought, the price paid, and the date of purchase, while the base USER holds login credentials and email address.

---

**USER_CARD }o--|| CHARACTER_CARD : "is based on"**
Each UserCard is based on exactly one character.  
A character card can have zero or more user cards associated with it.
This links a purchased card to a specific character, capturing its stats, rarity, archetype and other metadata.

---

**CHARACTERS }|--|| ARCHETYPE : "belongs to"**
Each character belongs to exactly one archetype.  
An Archetype is assigned to one or more characters.
A character must have an archetype.
Archetypes store literary classifications (like “The Hero” or “The Shadow”) and traditional archetype traits for that classification. CHARACTER_CARD stores global availability for shop rotations and links to the archetype and rarity tables.

---

**CHARACTER_CARD }|--|| RARITY : "has"**
Each character is assigned exactly one rarity.
Rarity is assigned to one or more character cards.
Character cards must have a rarity.
RARITY defines the classification (Common, Uncommon, Rare, Epic, Legendary, Mythic), a numerical level, and a base price. This allows characters to be consistently valued and ordered in the shop.

---

**SHOP_SCHEDULER ||--|{ SHOP_SCHEDULE_ITEMS : "has"**
A schop scheduler must include one or more schedule items.
One or more shop schedule items belong to a shop scheduler.
A shop scheduler must have at least one schedule item.
Stores per-rotation metadata, such as sale prices.

---

**CHARACTER_CARD 0{--||SHOP_SCHEDULE_ITEMS "appears in"**
Each character card can appear in zero or more schedule items.
Each schedule items corresponds to exactly one character. 
Characters can appear multiple times over time, but only once per shop scheduler. Also tracks rotation-specific details like sale price.

---

## **Testing**

### *User Story Testing*

### *Automated Testing*

#### **The W3C Markup Validation Service**

#### **The W3C CSS Validation Service**

#### **The JSHint Validation Service**

#### **CI Python Linter**

#### **JSONLint**
Used to format and validate JSON. 

#### **The WAVE Webb Accessibility Evaluation Tool**

#### **Chrome Lighthouse**

### **Manual Testing**

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
* [Paint.NET](http://Paint.NET)  
* [Psycopg2](https://pypi.org/project/psycopg2/)  
* [Python 3.13](https://www.python.org/)
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
* Help generating random choices from a list of objects
    * [geeksforgeeks](https://www.geeksforgeeks.org/python/python-select-random-value-from-a-list/)
    * [W3 Schools](https://www.w3schools.com/python/ref_random_choices.asp)
* Help understanding how to write a custom management command for importing json data into a model table:
    * [geeksforgeeks - how to import json to django model](https://www.geeksforgeeks.org/python/how-to-import-a-json-file-to-a-django-model/)
    * [codementor - data import from json](https://www.codementor.io/@happinessnwosuc/data-import-from-url-local-csv-and-json-files-into-db-django-app-d9z43iqbx)
    * [geeksforgeeks - custom management commands](https://www.geeksforgeeks.org/python/custom-django-management-commands/)
* Help understanding pathlib.Path - [geeksforgeeks](https://www.geeksforgeeks.org/python/get-parent-of-current-directory-using-python/)
* Handle() method typeError - [stackoverflow](https://stackoverflow.com/questions/41401202/django-command-throws-typeerror-handle-got-an-unexpected-keyword-argument)



## **Interesting Bugs**

## **Credits**

### *Data*

* Data for 731 superheroes and villains - [SuperHeroAPI](https://www.superheroapi.com/)

### *Media*

* Media for 731 superheroes and villains - [SuperHeroAPI](https://www.superheroapi.com/)
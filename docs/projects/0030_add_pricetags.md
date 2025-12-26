Read [@README.md](file:///Users/owenbrown/code/fairpay/README.md) and [@adr](file:///Users/owenbrown/code/fairpay/docs/adr) for context.

Our next step is to allow users to create a StoreVisit, upload PriceTag to the StoreVisit, and view a list of their StoreVisits. Do not add new model fields.

First step:
Update the Create Price Tag API route to accept store_visit_id, store this on the PriceTag, and return the created PriceTag timestamp.

Next, add "Create Store Visit" button to the logged-in user's home screen. Use a plain HTML POST form to create the StoreVisit and redirect to the new StoreVisit detail page. Use idiomatic Django trailing slashes in routes.

On the StoreVisit detail page, keep it simple. Display "Price Tags" with subtitle "Capture a picture of each price tag." Add button "Capture Price Tag." Use HTML to capture the price tag photo with the rear camera if possible. After capture, call the create-price-tag route and append the returned timestamp. Do not add camera checks.

See https://chatgpt.com/share/694effc5-75a4-8005-bc28-c51982df7b70

Read [@frontend_standards.md](file:///Users/owenbrown/code/fairpay/docs/archive/frontend_standards.md) . Do not use third party libraries. Keep the frontend as dumb as possible.

Next, add a "Prior Store Visits" button that links to a list of Store Visits.

Then, create "Store Visits" page that displays a table that lists each StoreVisit. Show:
- Store Visit Created at Time UTC isoformat is fine for now
- Number of Price Tags

Clicking on a Store Visit links to the store visit detail page. Newest first. The created_at should be the clickable link (no "View" text). Use idiomatic Django trailing slashes in routes.

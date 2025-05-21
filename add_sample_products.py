from app import app, db, Product

sample_products = [
    # Realistic High Shelf Items (bulky/overstock/less accessed)
    {
        'name': 'Bounty Paper Towels Mega Pack',
        'description': '12 double rolls of Bounty paper towels.',
        'price': 22.99,
        'shelf_location': '3rd Shelf',
        'stock': 8,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/bounty_paper_towels_mega_pack.jpg'
    },
    {
        'name': 'Charmin Ultra Soft Toilet Paper',
        'description': 'Mega roll, 24 count.',
        'price': 24.99,
        'shelf_location': '3rd Shelf',
        'stock': 10,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/charmin_ultra_soft_mega_roll.jpg'
    },
    {
        'name': 'Scott 1000 Toilet Paper 20-Pack',
        'description': '20 rolls of Scott 1000 toilet paper.',
        'price': 21.99,
        'shelf_location': '3rd Shelf',
        'stock': 7,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/scott_1000_20pack.jpg'
    },
    {
        'name': 'Sparkle Paper Towels 8-Pack',
        'description': '8 rolls of Sparkle paper towels.',
        'price': 13.99,
        'shelf_location': '3rd Shelf',
        'stock': 6,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/sparkle_paper_towels_8pack.jpg'
    },
    {
        'name': 'Brita Water Filter Pitcher',
        'description': 'Large Brita pitcher with filter.',
        'price': 29.99,
        'shelf_location': '3rd Shelf',
        'stock': 5,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/brita_water_filter_pitcher.jpg'
    },
    {
        'name': 'Kirkland Bottled Water 40-Pack',
        'description': '40 bottles of purified water.',
        'price': 5.99,
        'shelf_location': '3rd Shelf',
        'stock': 12,
        'category': 'Beverages',
        'high_shelf': True,
        'image_url': '/static/images/kirkland_bottled_water_40pack.jpg'
    },
    {
        'name': 'Tide Original Laundry Detergent (150 oz)',
        'description': 'Large jug for 96 loads.',
        'price': 19.99,
        'shelf_location': '3rd Shelf',
        'stock': 5,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/tide_original_150oz.jpg'
    },
    {
        'name': 'Arm & Hammer Laundry Detergent (170 oz)',
        'description': 'Bulk size, 110 loads.',
        'price': 17.99,
        'shelf_location': '3rd Shelf',
        'stock': 4,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/arm_hammer_laundry_170oz.jpg'
    },
    {
        'name': 'Hefty Ultra Strong Trash Bags (80 ct)',
        'description': 'Large box of 80 drawstring trash bags.',
        'price': 15.99,
        'shelf_location': '3rd Shelf',
        'stock': 6,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/hefty_ultra_strong_80ct.jpg'
    },
    {
        'name': 'Ziploc Freezer Bags Gallon (60 ct)',
        'description': 'Bulk box of gallon size freezer bags.',
        'price': 11.99,
        'shelf_location': '3rd Shelf',
        'stock': 8,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/ziploc_freezer_bags_gallon_60ct.jpg'
    },
    {
        'name': 'Swiffer WetJet Floor Cleaner Kit',
        'description': 'Starter kit with mop and cleaning solution.',
        'price': 27.99,
        'shelf_location': '3rd Shelf',
        'stock': 5,
        'category': 'Household',
        'high_shelf': True,
        'image_url': '/static/images/swiffer_wetjet_floor_cleaner_kit.jpg'
    },
    {
        'name': 'Huggies Snug & Dry Diapers Size 4 (124 ct)',
        'description': 'Large box of diapers.',
        'price': 39.99,
        'shelf_location': '3rd Shelf',
        'stock': 4,
        'category': 'Baby',
        'high_shelf': True,
        'image_url': '/static/images/huggies_snug_dry_size_4_124ct.jpg'
    },
    {
        'name': 'Pampers Swaddlers Diapers Size 5 (124 ct)',
        'description': 'Large box of Pampers diapers.',
        'price': 41.99,
        'shelf_location': '3rd Shelf',
        'stock': 4,
        'category': 'Baby',
        'high_shelf': True,
        'image_url': '/static/images/pampers_swaddlers_size_5_124ct.jpg'
    },
    {
        'name': 'Kellogg’s Frosted Flakes Family Size',
        'description': 'Large box of Frosted Flakes cereal.',
        'price': 6.49,
        'shelf_location': '3rd Shelf',
        'stock': 9,
        'category': 'Breakfast',
        'high_shelf': True,
        'image_url': '/static/images/kelloggs_frosted_flakes_family_size.jpg'
    },
    {
        'name': 'Cheerios Family Size Cereal',
        'description': 'Large box of Cheerios.',
        'price': 6.29,
        'shelf_location': '3rd Shelf',
        'stock': 8,
        'category': 'Breakfast',
        'high_shelf': True,
        'image_url': '/static/images/cheerios_family_size_cereal.jpg'
    },
    {
        'name': 'Keebler Club Crackers Family Pack',
        'description': 'Bulk box of Keebler Club Crackers.',
        'price': 8.99,
        'shelf_location': '3rd Shelf',
        'stock': 7,
        'category': 'Snacks',
        'high_shelf': True,
        'image_url': '/static/images/keebler_club_crackers_family_pack.jpg'
    },
    {
        'name': 'Lay’s Variety Pack Chips (28 ct)',
        'description': 'Bulk box of assorted Lay’s snack bags.',
        'price': 12.99,
        'shelf_location': '3rd Shelf',
        'stock': 6,
        'category': 'Snacks',
        'high_shelf': True,
        'image_url': '/static/images/lays_variety_pack_chips_28ct.jpg'
    },
    {
        'name': 'Seasonal Holiday Gift Wrap Set',
        'description': 'Assorted gift wrap, bows, and tags.',
        'price': 14.99,
        'shelf_location': '3rd Shelf',
        'stock': 7,
        'category': 'Seasonal',
        'high_shelf': True,
        'image_url': '/static/images/seasonal_holiday_gift_wrap_set.jpg'
    },

    # Regular Shelf Items
    {'name': 'Coca-Cola 6 Pack Bottles', 'description': '6 glass bottles of Coca-Cola.', 'price': 5.99, 'shelf_location': '2nd Shelf', 'stock': 10, 'category': 'Beverages', 'high_shelf': False, 'image_url': '/static/images/coca_cola_6pack_bottles.jpg'},
    {'name': 'Gatorade Orange 4-Pack', 'description': '4 bottles of Gatorade Orange.', 'price': 4.99, 'shelf_location': '2nd Shelf', 'stock': 8, 'category': 'Beverages', 'high_shelf': False, 'image_url': '/static/images/gatorade_orange_4pack.jpg'},
    {'name': 'Ritz Crackers', 'description': 'Classic round crackers.', 'price': 3.99, 'shelf_location': '1st Shelf', 'stock': 12, 'category': 'Snacks', 'high_shelf': False, 'image_url': '/static/images/ritz_crackers_box.jpg'},
    {'name': 'Quaker Oatmeal Variety Pack', 'description': 'Instant oatmeal, 18 packets.', 'price': 6.99, 'shelf_location': '2nd Shelf', 'stock': 7, 'category': 'Breakfast', 'high_shelf': False, 'image_url': '/static/images/quaker_oatmeal_variety_pack.jpg'},
    {'name': 'Crest Toothpaste 2-Pack', 'description': 'Crest whitening toothpaste, 2 tubes.', 'price': 6.49, 'shelf_location': '1st Shelf', 'stock': 9, 'category': 'Personal Care', 'high_shelf': False, 'image_url': '/static/images/crest_toothpaste_2pack.jpg'},
    {'name': 'Dove Body Wash', 'description': 'Dove moisturizing body wash, 22 oz.', 'price': 7.99, 'shelf_location': '1st Shelf', 'stock': 10, 'category': 'Personal Care', 'high_shelf': False, 'image_url': '/static/images/dove_body_wash_22oz.jpg'},
    {'name': 'Lysol Disinfectant Spray', 'description': 'Kills 99.9% of germs.', 'price': 8.99, 'shelf_location': '2nd Shelf', 'stock': 8, 'category': 'Household', 'high_shelf': False, 'image_url': '/static/images/lysol_disinfectant_spray.jpg'},
    {'name': 'Planters Mixed Nuts', 'description': 'Salted mixed nuts, 15 oz.', 'price': 7.49, 'shelf_location': '1st Shelf', 'stock': 11, 'category': 'Snacks', 'high_shelf': False, 'image_url': '/static/images/planters_mixed_nuts_15oz.jpg'},
    {'name': 'Hershey’s Milk Chocolate Bars', 'description': '6 pack of Hershey’s chocolate bars.', 'price': 4.99, 'shelf_location': '1st Shelf', 'stock': 13, 'category': 'Snacks', 'high_shelf': False, 'image_url': '/static/images/hersheys_milk_chocolate_bars_6pack.jpg'},
]

with app.app_context():
    # First, clear existing products
    Product.query.delete()
    
    # Add new sample products
    for product_data in sample_products:
        product = Product(**product_data)
        db.session.add(product)
    
    # Commit the changes
    db.session.commit()
    print("Sample products added successfully!")

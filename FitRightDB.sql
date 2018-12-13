
DROP TABLE IF EXISTS upper_body;
DROP TABLE IF EXISTS lower_body;
DROP TABLE IF EXISTS pattern;
DROP TABLE IF EXISTS material;
DROP TABLE IF EXISTS color;
DROP TABLE IF EXISTS product_item;
DROP TABLE IF EXISTS clothing_preferance;
DROP TABLE IF EXISTS profile;

-- This table holds the user id, full name, password, gender, age.
CREATE TABLE profile(
	profile_id INT(3) NOT NULL,
	profile_name VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	gender VARCHAR(6),
	age INT(5),
	PRIMARY KEY(profile_id, profile_name)
	
) ENGINE = InnoDB;

INSERT INTO profile VALUES 
(01, "Cole Kenworthy", "Cole 1996", "m", 22),
(02, "Leo La Rocca", "Password1", "m", 22),
(03, "Nick Mercadante", "Password", "m", 21),
(04, "Kailee Guerdette", "CarGirl15", "f", 21),
(05, "Gucci", "gucciguccigang", "b", 0),
(06, "Nike", "justdoit", "b", 0),
(07, "Calvin Klein", "ckforlife", "b", 0),
(08, "Old Navy", "oldnavy5", "b", 0)
;

--
--
--
-- Sources:
--
--
CREATE TABLE clothing_preferance(
	profile_id INT(3) NOT NULL,
	profile_name VARCHAR(50) NOT NULL,
	material VARCHAR(25),
	pattern VARCHAR(25),
	fit VARCHAR(25),
	color VARCHAR(20),
	lightness INT(1),
	price_min INT(8) DEFAULT(0),
	price_max INT(8) DEFAULT(100),
	
	PRIMARY KEY(profile_id, profile_name),
	FOREIGN KEY(profile_id, profile_name) REFERENCES profile(profile_id, profile_name)
	
) ENGINE = InnoDB;

INSERT INTO clothing_preferance VALUES 
(01, "Cole Kenworthy", "silk", "print", "slim", "black", 9, 10, 200),
(02, "Leo La Rocca", "cotton", "stripes", "relaxed", "green", 5, 50, 100),
(03, "Nick Mercadante", "leather", "dots", "regular", "red", 7, 100, 1000),
(04, "Kailee Guerdette", "spandex", "textile", "slim", "white", 1, 5, 50)

;

--
--
--
-- sources:
-- https://en.wikipedia.org/wiki/Fashion_design
--
--
CREATE TABLE product_item(
	item_id INT(3) NOT NULL,
	brand_id INT(3) NOT NULL,
	brand_name VARCHAR(50) NOT NULL,
	product_name VARCHAR(30),
	material VARCHAR(50),
	pattern VARCHAR(50),
	color VARCHAR(50),
	lightness INT(1),
	price INT(8),
	
	PRIMARY KEY (item_id, brand_id, brand_name),
	FOREIGN KEY (brand_id, brand_name) REFERENCES profile(profile_id, profile_name)
	
) ENGINE = InnoDB;

INSERT INTO product_item VALUES 
(01, 05, "Gucci", "Shirt", "silk", "print", "white", 8, 60),
(02, 06, "Nike", "Yoga pants", "spandex", "textile", "green", 5, 80),
(03, 07, "Calvin Klein", "Jacket","leather", "dots", "red", 4, 150),
(04, 08, "Old Navy", "Pants","cotton", "stripes", "black", 7, 20),
(05, 05, "Gucci", "Skinny Jeans","denim", "plain", "blue", 4, 20),

(06, 08, "Old Navy", "Sweatpants","cotton", "camouflage", "black", 7, 20),
(07, 06, "Nike", "Exercise Pants","spandex", "fractals", "blue", 7, 20),
(08, 07, "Calvin Klein", "Skirt","flannel", "zigzag", "red", 7, 20),
(09, 05, "Gucci", "Dress", "rayon", "dots", "black", 7, 20),
(10, 05, "Gucci", "Shirt", "cotton", "symmetrical", "white", 9, 70),
(11, 05, "Gucci", "Pants", "rayon", "stripes", "green", 7, 89),
(12, 05, "Gucci", "Slippers", "pvc", "stripes", "black", 1, 300),
(13, 05, "Gucci", "Gloves", "leather", "plaid", "brown", 4, 150),
(14, 05, "Gucci", "Jacket", "leather", "plain", "brown", 3, 200),
(15, 05, "Gucci", "Suit", "silk", "plaid", "green", 7, 450),
(16, 06, "Nike", "Shirt", "polyester", "print", "white", 8, 39),
(17, 06, "Nike", "Shorts", "cotton", "fractals", "red", 5, 49),
(18, 06, "Nike", "Pants", "cotton", "plain", "black", 3, 60),
(19, 06, "Nike", "Jacket", "pvc", "lines", "green", 7, 90),
(20, 06, "Nike", "Shoes", "polyester", "plaid", "green", 7, 250),
(21, 07, "Calvin Klein", "Suit", "wool", "plain", "blue", 4, 350),
(22, 07, "Calvin Klein", "Shirt", "silk", "textile", "white", 9, 89),
(23, 07, "Calvin Klein", "Pants", "silk", "plaid", "blue", 7, 79),
(24, 07, "Calvin Klein", "Shoes", "leather", "plain", "brown", 5, 250),
(25, 08, "Old Navy", "Sweatshirt", "cotton", "camouflage", "green", 7, 55),
(26, 08, "Old Navy", "Shirt", "polyester", "print", "cyan", 4, 35),
(27, 08, "Old Navy", "Shorts", "cotton", "lines", "yellow", 8, 40),
(28, 08, "Old Navy", "Jacket", "pvc", "plaid", "magenta", 5, 20),
(29, 08, "Old Navy", "Socks", "wool", "camouflage", "black", 3, 10),
(30, 08, "Old Navy", "Jeans", "denim", "plain", "blue", 5, 50),
(31, 08, "Old Navy", "Jacket", "denim", "print", "blue", 5, 60);


-- This is a list of the colors used in clothing by each brand. This list 
-- includeds the three primary colors (red, green, blue), three secondary
-- (cyan, magenta, yellow), black, white, grey, brown. With lightness denoting 
-- different shades of one color 0=black, color starting at 1 ends at 8 ,white=9
-- The defult value for color lightness is 5. IE brown 5 is normal brown.
-- Where brown 7 is tan. this is low value, match the color then lightness.
-- If lightness values don't match still show the option of it.
-- sources:
-- https://www.usability.gov/how-to-and-tools/methods/color-basics.html
-- https://en.wikipedia.org/wiki/Clothing_material
CREATE TABLE color(
	c_id INT (3),
	c_name VARCHAR (50),
	lightness int(1) DEFAULT (5),
		CONSTRAINT CHK_lightness CHECK (lightness IN (0, 1, 2, 3, 4, 5, 6,
		7, 8, 9)),
	color_type VARCHAR(17) NOT NULL,
		CONSTRAINT CHK_color_type CHECK (color_type IN ('red', 'blue', 
		'green', 'yellow', 'white', 'black', 'grey', 'cyan', 'magenta',
		'pink',	'violet', 'purple', 'orange', 'brown' )),
	
	PRIMARY KEY (c_id, color_type),
	FOREIGN KEY (c_id, c_name) REFERENCES product_item (brand_id, brand_name)
	
) ENGINE = InnoDB;

INSERT INTO color VALUES 
(05, "Gucci", 9, "white"),
(05, "Gucci", 7, "green"),
(05, "Gucci", 2, "black"),
(05, "Gucci", 5, "red"),
(06, "Nike", 2, "black"),
(06, "Nike", 5, "white"),
(06, "Nike", 5, "grey"),
(06, "Nike", 5, "blue"),
(06, "Nike", 5, "green"),
(07, "Calvin Klein", 5, "red"),
(07, "Calvin Klein", 2, "black"),
(07, "Calvin Klein", 7, "blue"),
(07, "Calvin Klein", 9, "white"),
(07, "Calvin Klein", 5, "green"),
(07, "Calvin Klein", 3, "brown"),
(08, "Old Navy", 6, "green"),
(08, "Old Navy", 5, "red"),
(08, "Old Navy", 1, "black"),
(08, "Old Navy", 6, "blue"),
(08, "Old Navy", 9, "white"),
(08, "Old Navy", 4, "grey")
;


-- is a list of materials that are used in clothing. this list is tied to the 
-- brand that makes clothing, and is used to check if the user preference 
-- is in the list. the user is limited to entering the primary material,
-- restricted to cotton, flax, wool, silk, ramie, denim, leather, down, fur,
-- rayon, nylon, polyester, spandex, flannel, lyocell, pvc, bamboo, 
-- jute, hemp, tyvek, jute. list comes from this link.
-- sources:
-- https://en.wikipedia.org/wiki/Clothing_material
CREATE TABLE material(
	m_id INT (3),
	m_name VARCHAR (50),
	material_type VARCHAR(17) NOT NULL,
		CONSTRAINT CHK_material_type CHECK (material_type IN ('cotton', 'flax', 
		'wool', 'silk', 'ramie', 'denim', 'leather', 'down', 'fur', 'rayon',
		'nylon', 'polyester', 'spandex', 'flannel', 'lyocell', 'pvc', 
		'recycled cotton', 'bamboo', 'jute', 'hemp', 'tyvek')),
	
	PRIMARY KEY (m_id, material_type),
	FOREIGN KEY (m_id, m_name) REFERENCES product_item (brand_id, brand_name)
) ENGINE = InnoDB;

INSERT INTO material VALUES 
(05, "Gucci", "silk"),
(05, "Gucci", "polyester"),
(05, "Gucci", "bamboo"),
(05, "Gucci", "leather"),
(06, "Nike", "spandex"),
(06, "Nike", "cotton"),
(06, "Nike", "polyester"),
(06, "Nike", "tyvek"),
(06, "Nike", "rayon"),
(07, "Calvin Klein", "silk"),
(07, "Calvin Klein", "polyester"),
(07, "Calvin Klein", "wool"),
(07, "Calvin Klein", "denim"),
(07, "Calvin Klein", "leather"),
(07, "Calvin Klein", "cotton"),
(08, "Old Navy", "cotton"),
(08, "Old Navy", "denim"),
(08, "Old Navy", "leather"),
(08, "Old Navy", "wool"),
(08, "Old Navy", "flannel"),
(08, "Old Navy", "polyester")
;

-- This is a list of the patterns used by a brand in their clothing. Each brand_id
-- and name are linked to a preset pattern that can be selected. Patterns are
-- restricted to the values of dots(polka dot, halftone), 
-- Textile patterns(adinkra sysmbols, argyle, border tartan, check, glen plaid, 
-- gul, harlequin print, tweed, embroidery, houndstooth, paisley, stripes, rain
-- tartan, celtic maze), camouflage, symmetrical, fractals, spirals, waves, 
-- bubbles, cracks, line, zigzag, plain, print.
-- sources:
-- https://en.wikipedia.org/wiki/Category:Dot_patterns
-- https://en.wikipedia.org/wiki/Category:Textile_patterns
-- https://en.wikipedia.org/wiki/Patterns_in_nature
-- https://en.wikipedia.org/wiki/Category:Patterns
CREATE TABLE pattern(
	p_id INT (3),
	p_name VARCHAR (50),
	pattern_type VARCHAR(20) NOT NULL,
		CONSTRAINT CHK_pattern CHECK (pattern_type IN ('dots', 'textile', 
		'camouflage', 'semmetrical', 'spirals', 'waves', 'bubbles', 'cracks',
		'lines', 'zigzag', 'fractals', 'plain', 'print')),
	PRIMARY KEY (p_id, pattern_type),
	FOREIGN KEY (p_id, p_name) REFERENCES product_item (brand_id, brand_name)

) ENGINE = InnoDB;

INSERT INTO pattern VALUES 
(05, "Gucci", "textile"),
(05, "Gucci", "plain"),
(05, "Gucci", "print"),
(05, "Gucci", "semmetrical"),
(06, "Nike", "plain"),
(06, "Nike", "print"),
(06, "Nike", "lines"),
(06, "Nike", "dots"),
(06, "Nike", "fractals"),
(07, "Calvin Klein", "textile"),
(07, "Calvin Klein", "plain"),
(07, "Calvin Klein", "print"),
(07, "Calvin Klein", "zigzag"),
(07, "Calvin Klein", "lines"),
(07, "Calvin Klein", "waves"),
(08, "Old Navy", "zigzag"),
(08, "Old Navy", "camouflage"),
(08, "Old Navy", "print"),
(08, "Old Navy", "spirals"),
(08, "Old Navy", "textile"),
(08, "Old Navy", "bubbles")
;

-- Aim to match people based on chest first. Then neck_to_wrist, back_to_waist, arm_length.
-- Other values are used for custom items.
-- all done in inches
-- Sources:
--
CREATE TABLE upper_body(
	ub_id INT(4) NOT NULL,
	ub_name VARCHAR(50) NOT NULL,
	company BOOLEAN,
	size_def CHAR(2),
	chest DOUBLE(4,1),
	neck_to_wrist DOUBLE(4,1),
	back_to_waist DOUBLE(4,1),
	cross_back DOUBLE(4,1),
	hand_cicurm DOUBLE(4,1),
	wrist_cicurm DOUBLE(4,1),
	hand_length DOUBLE(4,1),
	arm_length DOUBLE(4,1),
	upper_arm DOUBLE(4,1),
	arm_hole_depth DOUBLE(4,1),
	
	PRIMARY KEY (ub_id, ub_name),
	FOREIGN KEY (ub_id, ub_name) REFERENCES profile (profile_id, profile_name)
) ENGINE = InnoDB;

INSERT INTO upper_body VALUES 
(01, "Cole Kenworthy", '0', "L", 36, 45, 33, 35, 7, 4, 8, 27, 15, 7),
(02, "Leo La Rocca", '0', "XL", 40, 50, 36, 39, 10, 6, 10, 30, 19, 9),
(03, "Nick Mercadante", '0', "m", 32, 40, 30, 31, 5, 3, 7, 24, 12, 5),
(04, "Kailee Guerdette", '0', "s", 30, 38, 28, 30, 5, 3, 6, 24, 10, 5),
(05, "Gucci", '1', "L", 36, 45, 33, 35, 7, 4, 8, 27, 15, 7),
(06, "Nike", '1', "s", 30, 38, 28, 30, 5, 3, 6, 24, 10, 5),
(07, "Calvin Klein", '1', "m", 32, 40, 30, 31, 5, 3, 7, 24, 12, 5),
(08, "Old Navy", '1', "XL", 40, 50, 36, 39, 10, 6, 10, 30, 19, 9);

-- Value the waist, instep, thigh, side_length for match, +-2 inches is good range
-- Other values are used for custom fit clothing
-- waist value is from standard sizing ie 32 for men and 0-10 range for women
-- All measurements in inches
CREATE TABLE lower_body(
	lb_id INT(4) NOT NULL,
	lb_name VARCHAR(50) NOT NULL,
	company BOOLEAN,
	waist DOUBLE(4,1),
	hips DOUBLE(4,1),
	thigh DOUBLE(4,1),
	knee DOUBLE(4,1),
	calf DOUBLE(4,1),
	instep DOUBLE(4,1),
	side_to_knee DOUBLE(4,1),
	side_length DOUBLE(4,1),
	crotch_depth DOUBLE(4,1),
	crotch_length DOUBLE(4,1),
	
	PRIMARY KEY (lb_id, lb_name),
	FOREIGN KEY (lb_id, lb_name) REFERENCES profile(profile_id, profile_name)
	
) ENGINE = InnoDB;

INSERT INTO lower_body VALUES 
(01, "Cole Kenworthy", '0', 32, 33, 25, 15, 14, 30, 16, 35, 10, 12),
(02, "Leo La Rocca", '0', 34, 35, 24, 15, 12, 32, 18, 37, 12, 14),
(03, "Nick Mercadante", '0', 30, 28, 20, 13, 10, 28, 14, 33, 8, 10),
(04, "Kailee Guerdette", '0', 0, 33, 22, 13, 14, 25, 13, 28, 7, 9),
(05, "Gucci", '1', 32, 33, 25, 15, 14, 30, 16, 35, 10, 12),
(06, "Nike", '1', 0, 33, 22, 13, 14, 25, 13, 28, 7, 9),
(07, "Calvin Klein", '1', 30, 28, 20, 13, 10, 28, 14, 33, 8, 10),
(08, "Old Navy", '1', 34, 35, 24, 15, 12, 32, 18, 37, 12, 14);

--ncreate our DB content

CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64),
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

-- create dommy test with 
INSERT INTO task (
    name,
    summary,
    description
) VALUES
(
    "Wash the car",
    "Take the car to the car wash",
    "make sure it gets vaccummed and waxed"
),
(
    "Walk the dog",
    "Fido needs daily exercise",
    "fido must take 3 laps around the park"
),
(
    "Buy groceries",
    "Go to the supermarket",
    "We need: eggs, milk, tomatoes and becan"
);

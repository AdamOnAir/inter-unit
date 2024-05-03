pub fn fh_kelvin(fahreneit: f64) -> f64 {
	let kelvin = (fahreneit - 32.0) * 5.0 / 9.0 + 273.15;
	kelvin
}

pub fn celsuis_kelvin(celsuis: f64) -> f64 {
	let kelvin = celsuis + 273.15;
	kelvin
}

pub fn lb_kg(lbs: f64) -> f64 {
	let kg = lbs / 2.205;
	kg
}


pub fn gallon_liter(gallon: f64) -> f64 {
	let liter = gallon / 3.785412;
	liter
}

pub fn feet_m(feet: f64) -> f64 {
	let m = feet / 3.28084;
	m
}

// Length
pub fn mile_km(mile: f64) -> f64 {
	let km = mile * 1.609;
	km
}

pub fn inch_cm(inch: f64) -> f64 {
	let cm = inch * 2.54;
	cm
}

pub fn nmile_km(nautical: f64) -> f64 {
	let km = nautical * 1.852;
	km
}

pub fn pascal_bar(pascal: f64) -> f64 {
	let bar = pascal / 100000.0;
	bar
}

pub fn liter_cubic(liter: f64) -> f64 {
	let cubic = liter / 1000.0;
	cubic
}

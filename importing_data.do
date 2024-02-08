import delimited "C:\Users\Balazs_Tibor\Desktop\coding_for_econ_stata\coding_for_economists\data\raw\european_commission\ted-sample.csv", clear

keep iso_country_code win_country_code award_value_euro

summarize award_value_euro, detail
display "number of observations `r(n)'"
display "mean: `r(mean)'"

generate above_mean=1

drop if award_value_euro > `r(p95)' 

hist award_value_euro

*replace above_mean=0 if award_value_euro < `r(p50)'
*replace above_mean=0

forvalues i = 0/9 {
	display `i'}
	
foreach vegetable in paprika aubergine carrot {
	di "`vegetable'"
}

*foreach2

foreach var of varlist iso_country_code win_country_code {
	count if strlen(`var') > 2
}




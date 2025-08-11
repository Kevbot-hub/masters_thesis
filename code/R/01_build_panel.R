
library(tidyverse)
dir.create("data/clean", showWarnings = FALSE, recursive = TRUE)
panel <- tibble(
  country = character(),
  quarter = character(),
  capability_area = character(),
  shock_event = integer(),
  shock_severity = integer(),
  pre_shock_us_exposure = double(),
  pesco_projects = integer(),
  edf_awards_count = integer(),
  collab_proc_share = double(),
  eu_origin_proc_share = double(),
  autonomy_rhetoric_index = double(),
  threat_alignment = double(),
  defence_spend_gdp = double(),
  industry_capacity = double()
)
write_csv(panel, "data/clean/country_quarter_panel.csv")
message("Wrote data/clean/country_quarter_panel.csv")

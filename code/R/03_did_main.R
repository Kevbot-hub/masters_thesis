
library(tidyverse); library(fixest)
stopifnot(file.exists("data/clean/country_quarter_panel.csv"))
df <- readr::read_csv("data/clean/country_quarter_panel.csv")
# TODO: feols(...) once panel is populated
message("DiD placeholder - implement once panel is populated.")

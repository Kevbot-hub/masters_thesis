
library(tidyverse)
stopifnot(file.exists("data/clean/country_quarter_panel.csv"))
df <- readr::read_csv("data/clean/country_quarter_panel.csv")
# TODO: implement event-time computation and plot
ggplot() + ggtitle("Event Study Placeholder") +
  xlab("Event Time (quarters)") + ylab("Outcome")
ggplot2::ggsave("docs/event_study_placeholder_R.png", dpi = 200, width = 6, height = 4)
message("Wrote docs/event_study_placeholder_R.png")

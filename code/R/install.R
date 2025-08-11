
# Install required R packages
packages <- c("tidyverse","fixest","did","data.table","readr","ggplot2")
to_install <- packages[!(packages %in% installed.packages()[,"Package"])]
if(length(to_install)) install.packages(to_install, repos="https://cloud.r-project.org")
message("R packages ready.")

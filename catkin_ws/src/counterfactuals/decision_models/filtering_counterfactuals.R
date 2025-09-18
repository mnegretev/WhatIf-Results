# Loading required library
library(dplyr)

# Reading the counterfactuals_complete.R file (assuming it's a CSV file)
counterfactuals <- read.csv("counterfactuals_complete.csv")

# Filtering rows where best_intervention is "*"
filtered_data <- counterfactuals %>% 
  filter(best_intervention == "*")

# Selecting all columns except the specified ones
result <- filtered_data %>% 
  select(-c(probability, elapsed_time, group_id, ranking, 
            potential_crash_before_intervention, 
            potential_crash_after_intervention, 
            best_intervention))

# Saving the resulting dataframe to a new CSV file
write.csv(result, "counterfactuals.csv", row.names = FALSE)

# Printing a message to confirm completion
cat("Filtered data saved to filtered_counterfactuals.csv\n")

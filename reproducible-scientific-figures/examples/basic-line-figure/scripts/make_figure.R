library(ggplot2)

dir.create("outputs", showWarnings = FALSE, recursive = TRUE)
df <- read.csv("data/figure_ready_data.csv")

p <- ggplot(df, aes(x = year, y = response_index, color = treatment, group = treatment)) +
  geom_line(linewidth = 0.7) +
  geom_point(size = 2) +
  scale_x_continuous(breaks = sort(unique(df$year))) +
  labs(
    x = "Year",
    y = "Response index",
    color = "Treatment"
  ) +
  theme_classic(base_size = 9)

ggsave("outputs/Fig_Example_1.svg", p, width = 90, height = 65, units = "mm")
ggsave("outputs/Fig_Example_1_preview.png", p, width = 90, height = 65, units = "mm", dpi = 300)

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}
library(ggplot2)

setwd("C:/Users/maell/OneDrive/Documents/Master2/Statistiques de variations/")

files <- c(
  "CAI_Result_Pyogenes.txt",
  "CAI_Result_Pneumo.txt",
  "CAI_Result_Agalactiae.txt",
  "CAI_Result_Lactis.txt",
  "CAI_Result_Penangensis.txt"
)

all_values <- list()

for (file in files) {
  values <- read.table(file, header = FALSE)$V4
  all_values <- c(all_values, list(values))
}

df <- data.frame(Organisme = rep(files, sapply(all_values, length)),
                 Valeurs_CAI = unlist(all_values))

df$Groupe <- ifelse(df$Organisme %in% c("CAI_Result_Pyogenes.txt"), "Organisme étudié",
                    ifelse(df$Organisme %in% c("CAI_Result_Agalactiae.txt", "CAI_Result_Pneumo.txt"), "Organismes du même genre Streptococcus",
                           ifelse(df$Organisme %in% c("CAI_Result_Penangensis.txt", "CAI_Result_Lactis.txt"), "Organismes de la même famille Streptococcaceae", NA)))

colors <- c("Organisme étudié" = "blue", 
            "Organismes du même genre Streptococcus" = "red", 
            "Organismes de la même famille Streptococcaceae" = "green")

plot <- ggplot(df, aes(x = factor(Organisme, levels = files), y = Valeurs_CAI, fill = Groupe)) +
  geom_violin(alpha = 0.5) +
  geom_boxplot(width = 0.2, position = position_dodge(0.75), alpha = 0.5) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        panel.grid.major = element_line(color = "gray", linetype = "dashed", size = 0.5), 
        plot.title = element_text(hjust = 0.5)) +
  scale_fill_manual(values = colors) +
  labs(
    x = "Organisme",
    y = "Valeurs de CAI",
    title = "Violin Plot des CAI (Codon Adaptation Usage)",
    fill = "Classification"
  ) +
  theme(legend.position = "bottom", 
        legend.title = element_text(size = 10),
        legend.text = element_text(size = 8))

plot <- plot +
  scale_x_discrete(labels = c(
    "CAI_Result_Pyogenes.txt" = "S. pyogenes",
    "CAI_Result_Pneumo.txt" = "S. pneumoniae",
    "CAI_Result_Agalactiae.txt" = "S. agalactiae",
    "CAI_Result_Lactis.txt" = "L. lactis",
    "CAI_Result_Penangensis.txt" = "F. penangensis"
  ))

print(plot)

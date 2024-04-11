library(reticulate)
# I have to specify this because I have different versions of python on my machine, not sure if needed elsewhere
use_python("/usr/bin/python3", required = TRUE)

# Source the Python script
source_python("./P.py")

file <- "../test1.zc"
output_path <- "output_zc_plot.png"

# Execute Python functions
rf <- read_zc(file)
t<-rf[[1]]
f<-rf[[2]]
plot_zc(t, f, pngpath=output_path)

cat("Plot saved to:", output_path, "\n")

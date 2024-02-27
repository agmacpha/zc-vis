library(bioacoustics)
library(tidyverse)

#Create the zc from Anabat
#Read the zc

file <- "/users/alexandremacphail/desktop/zc/2020-07-22 03-09-40_00000_000.00#"
z <- read_zc(file)

zc_data <- list(raw = raw <- readBin(file, what = "integer", n = 16384, size = 1, signed = FALSE))
md <- list( file = list(FTYPE = FTYPE <- raw[4]) )

ggplot(z, aes(x=z$data$time_data, y=z$data$freq_data))

time <- z$data$time_data %>% as_tibble_col("time") %>% mutate(time = time / 10e6)
freq <- z$data$freq_data %>% as_tibble_col("freq")

z1 <- bind_cols(time, freq) %>% na.omit()

ggplot(z1, aes(x=time,y=freq)) + geom_point() + theme_bw()
plot_zc(z, dot.size = 0.6)

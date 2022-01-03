#Reshape the bird images for qualtrics!

library(tidyverse)

birds <- read_tsv('~/Repositories/bird_data/e2_ebirds-qualtrics/qualtrics_images.csv', 
                  col_names = c("image","image_url")) %>%
  separate(image, into = c("species_code", "image_number"), extra = 'drop')
  
birds <- birds %>%
  pivot_wider(names_from = image_number, values_from = image_url, names_prefix = "picture_")

write_tsv(birds, file = '~/Repositories/bird_data/e2_ebirds-qualtrics/qualtrics_images_reshaped.csv')

# condition_palette <- c(control = 'grey80', depletion = 'black')
# condition_palette_red <- c(control = 'grey80', depletion = '#D55E00')
# condition_shape = c( control = 8, depletion = 19)

# cell_type_palette <- c(t_cell = "#739C83", cyto_t_cell = "#739C83", b_cell = "#CF6C59")

# Scater palettes.
# Obtained from : https://github.com/alanocallaghan/scater/blob/devel/R/plot_colours.R
get_scater_palette <- function(palette_name)
  # Function to define colour palettes.
{
  switch(palette_name,
         tableau20 = c("#1F77B4", "#AEC7E8", "#FF7F0E", "#FFBB78", "#2CA02C",
                       "#98DF8A", "#D62728", "#FF9896", "#9467BD", "#C5B0D5",
                       "#8C564B", "#C49C94", "#E377C2", "#F7B6D2", "#7F7F7F",
                       "#C7C7C7", "#BCBD22", "#DBDB8D", "#17BECF", "#9EDAE5"),
         tableau10medium = c("#729ECE", "#FF9E4A", "#67BF5C", "#ED665D",
                             "#AD8BC9", "#A8786E", "#ED97CA", "#A2A2A2",
                             "#CDCC5D", "#6DCCDA"),
         colorblind10 = c("#006BA4", "#FF800E", "#ABABAB", "#595959",
                          "#5F9ED1", "#C85200", "#898989", "#A2C8EC",
                          "#FFBC79", "#CFCFCF"),
         colourblind10 = c("#006BA4", "#FF800E", "#ABABAB", "#595959",
                           "#5F9ED1", "#C85200", "#898989", "#A2C8EC",
                           "#FFBC79", "#CFCFCF"),
         trafficlight = c("#B10318", "#DBA13A", "#309343", "#D82526",
                          "#FFC156", "#69B764", "#F26C64", "#FFDD71",
                          "#9FCD99"),
         purplegray12 = c("#7B66D2", "#A699E8", "#DC5FBD", "#FFC0DA",
                          "#5F5A41", "#B4B19B", "#995688", "#D898BA",
                          "#AB6AD5", "#D098EE", "#8B7C6E", "#DBD4C5"),
         bluered12 = c("#2C69B0", "#B5C8E2", "#F02720", "#FFB6B0", "#AC613C",
                       "#E9C39B", "#6BA3D6", "#B5DFFD", "#AC8763", "#DDC9B4",
                       "#BD0A36", "#F4737A"),
         greenorange12 = c("#32A251", "#ACD98D", "#FF7F0F", "#FFB977",
                           "#3CB7CC", "#98D9E4", "#B85A0D", "#FFD94A",
                           "#39737C", "#86B4A9", "#82853B", "#CCC94D"),
         cyclic = c("#1F83B4", "#1696AC", "#18A188", "#29A03C", "#54A338",
                    "#82A93F", "#ADB828", "#D8BD35", "#FFBD4C", "#FFB022",
                    "#FF9C0E", "#FF810E", "#E75727", "#D23E4E", "#C94D8C",
                    "#C04AA7", "#B446B3", "#9658B1", "#8061B4", "#6F63BB"),
         okabeito = c("#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000")

  )
}


sample_type_barcode_palette <- c(
  ctc_cluster = "#FFBB78",
  ctc_cluster_heterotypic = "#F02720",
  ctc_cluster_wbc = "#FF9C0E",
  ctc_cluster_dn = "#FF9C0E",
  ctc_single =  "#2CA02C",
  ctc_gfp =  "#2CA02C",
  ctc_single_pool = "#2CA02C",
  cto = "#9467BD",
  cto_heterotypic = "#C5B0D5",
  cto_wbc  = "#B446B3",
  dn_cell = "#898989",
  dn_cluster_heterotypic = "#898989",
  `Single CTC` = "#2CA02C",
  `CTC cluster` = "#FF9C0E",
  `CTO` = "#9467BD"
)


bc_group_palette = c(
  `CTC` = "#ff7b7b",
  `ST` = "#B5DFFD",
  CAF = 'black',
  other = 'white',
  `CTC_CAF` = '#E7B800',
  `ST_CAF` = 'grey50'
)



bc_group_cluster_palette = c(
  `CTC1` = "#A40905",
  `CTC2` = "#F4A3A3",
  `CTC3` = "#AD8BC9",
  `ST` = "#B5DFFD",
  `PT ref` = "#B5DFFD",
  CAF = '#E69F00',
  `CTC1_CAF` = '#f59342',
  `CTC2_CAF` = '#E7B800',
  `CTC3_CAF` = '#c19ce6',
  `ST_CAF` = '#c19ce6',
  other = '#e5e5e5'
)

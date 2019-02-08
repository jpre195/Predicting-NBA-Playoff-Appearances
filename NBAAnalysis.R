# Data extracted from https://www.basketball-reference.com/leagues/NBA_2018.html

#############################
### Set working directory ###
#############################

setwd("C:\\Users\\Jdpre\\Desktop\\Multivariate Analysis")

#########################
### Required Packages ###
#########################

library(XML)
library(RCurl)
library(rlist)
library(rvest)
library(xlsx)
library(tidyverse)
library(MASS)
library(ggplot2)
library(car)
library(glmulti)

#################
### Functions ###
#################

random_indeces <- function(n, k) {
  sample(1:n, k, replace = FALSE)
}

confusion <- function(actual, predicted, names = NULL, printit = TRUE,
                      prior = NULL) {
  if (is.null(names))
    names <- levels(actual)
    tab <- table(actual, predicted)
    acctab <- t(apply(tab, 1, function(x) x/sum(x)))
    dimnames(acctab) <- list(Actual = names, "Predicted (cv)" = names)
    if (is.null(prior)) {
      relnum <- table(actual)
      prior <- relnum/sum(relnum)
      acc <- sum(tab[row(tab) == col(tab)])/sum(tab)
      }
    else {
      acc <- sum(prior * diag(acctab))
      names(prior) <- names
      }
    if (printit)
      print(round(c("Overall accuracy" = acc, "Prior frequency" = prior),
                    4))
    if (printit) {
      cat("\nConfusion matrix", "\n")
      print(round(acctab, 4))
      }
    invisible(acctab)
    }

########################
### Read in the data ###
########################

nba_team_data <- read.xlsx("NBA_Team_Data1.xlsx", sheetIndex = 1, header = TRUE, startRow = 2)

for(i in 2:10) {
  curr_table <- read.xlsx(paste("NBA_Team_Data", i, ".xlsx", sep = ""), sheetIndex = 1, header = TRUE, startRow = 2)
  nba_team_data <- rbind(nba_team_data, curr_table)
}

nba_team_data <- nba_team_data[nba_team_data$Team != "League Average",]

current_team_data <- read.xlsx("C:\\Users\\Jdpre\\Desktop\\Multivariate Analysis\\Current_NBA_Team_Data.xlsx", sheetIndex = 1, header = TRUE, startRow = 2)

current_team_data <- current_team_data[current_team_data$Team != "League Average",]

#######################
### Format the data ###
#######################

nba_team_data <- separate(nba_team_data, col = Team, into = c("Team", "Playoffs"), sep = "\\*")

for(i in 1:nrow(nba_team_data)) {
  if(is.na(nba_team_data[i, "Playoffs"])) {
    nba_team_data[i, "Playoffs"] = 0
  } else {
    nba_team_data[i, "Playoffs"] = 1
  }
}

nba_team_data <- mutate(nba_team_data, W_Perc = W / 82)

nba_team_data <- subset(nba_team_data, select = -c(Rk, PW, PL, L, Attend., W))

training_indeces <- random_indeces(nrow(nba_team_data), .85*nrow(nba_team_data))

nba_team_data_train <- nba_team_data[training_indeces,]

nba_team_data_test <- nba_team_data[-training_indeces,]

current_team_data <- mutate(current_team_data, W_Perc = W / (W + L))

current_team_data <- subset(current_team_data, select = -c(Rk, PW, PL, L, Attend., W))

#####################################
### Principal Components Analysis ###
#####################################

pca1 <- subset.data.frame(nba_team_data_train, select = -c(Team, Playoffs, Year, Arena, W_Perc, ORtg, DRtg))

nba_team_data.pca1 <- prcomp(pca1, center = TRUE, scale. = TRUE)

data_summ <- summary(nba_team_data.pca1)

screeplot(nba_team_data.pca1)

screeplot_y <- data_summ$importance[2,]

screeplot_tidy <- gather(as.data.frame(screeplot_y), key = "PrinComp", value = "Percent_Variation")

screeplot_tidy$PrinComp <- seq(1, 17)

ggplot(screeplot_tidy, aes(x = PrinComp, y = Percent_Variation)) + geom_line(lwd = 1.025) + geom_point(size = 2) + geom_vline(xintercept = 4, color = "red", lwd = 1.025) + scale_x_continuous(name='Principal Component Number', breaks=1:17) + ggtitle("Scree Plot for NBA Team Data") + ylab("Proportion of Variation")

# Show there are 4 principal components
# First 4 PC account for 67% of the variation

#######################
### Factor Analysis ###
#######################

nba_team_data.fact1 <- factanal(pca1, 4)

# 4 main factors appear to be: Offensive Efficiency, Defensive Efficiency, Free Throw Efficiency,
#                              Strength of Schedule

##############################
### MV Regression Analysis ###
##############################

y <- subset(nba_team_data_train, select = c(W_Perc, ORtg, DRtg))

y <- as.matrix(y)

X <- pca1

X <- as.matrix(X)

beta_hat <- solve(t(X) %*% X) %*% t(X) %*% y

beta_hat <- as.matrix(beta_hat)

nba_team_data_test_y <- subset(nba_team_data_test, select = c(W_Perc, ORtg, DRtg))

nba_team_data_test_y <- as.matrix(nba_team_data_test_y)

nba_team_data_test_X <- subset.data.frame(nba_team_data_test, select = -c(Playoffs, Team, Year, Arena, W_Perc, ORtg, DRtg))

nba_team_data_test_X <- as.matrix(nba_team_data_test_X)

nba_team_data_test_fit <- nba_team_data_test_X %*% beta_hat # Model made by hand




nba_team_data_test_fit2 <- lm(cbind(W_Perc, ORtg, DRtg) ~ Age + MOV + SOS + SRS + Pace + FTr + X3PAr + TS. + eFG. + TOV. + ORB. + FT.FGA + eFG..1 + TOV..1 + DRB. + FT.FGA.1 + Attend..G, data = nba_team_data_train)

summary(nba_team_data_test_fit2)

Manova(nba_team_data_test_fit2) # Remove MOV, Pace, eFG., Attend..G

alias(nba_team_data_test_fit2)



nba_team_data_test_fit3 <- lm(cbind(W_Perc, ORtg, DRtg) ~ Age + SOS + SRS + FTr + X3PAr + TS. + TOV. + ORB. + FT.FGA + eFG..1 + TOV..1 + DRB. + FT.FGA.1, data = nba_team_data_train)

Manova(nba_team_data_test_fit3) # Best model

alias(nba_team_data_test_fit3)

coefficients(nba_team_data_test_fit3)

residuals(nba_team_data_test_fit3)

influence(nba_team_data_test_fit3)

nba_team_data_test_fit3.stdres <- rstandard(nba_team_data_test_fit3)

shapiro.test(nba_team_data_test_fit3.stdres)

qqnorm(nba_team_data_test_fit3.stdres)

qqline(nba_team_data_test_fit3.stdres)

fitted_nba_team_data_test <- predict(nba_team_data_test_fit3, nba_team_data_test)

coef(summary(nba_team_data_test_fit3))

summary(nba_team_data_test_fit3)




cor(nba_team_data_test_y, nba_team_data_test_fit)

cor(fitted_nba_team_data_test, nba_team_data_test_y)

#############################
### Discriminant Analysis ###
#############################

da1 <- subset(nba_team_data_train, Team != "League Average", select = -c(Team, Playoffs, Year, Arena))

da1_y <- nba_team_data_train$Playoffs

prior <- c(14/30, 16/30)

lda_fit <- lda(da1_y ~ Age + MOV + SOS + SRS + ORtg + DRtg + Pace + FTr + X3PAr + TS. + eFG. + TOV. + ORB. + FT.FGA + eFG..1 + TOV..1 + DRB. + FT.FGA.1 + Attend..G + W_Perc, data = da1, prior = prior)

coef(lda_fit)

nba_team_data_test_fit <- predict(lda_fit, nba_team_data_test)

nba_team_data_test_lda_predicted <- rep(0, nrow(nba_team_data_test_fit$posterior))

for(i in 1:length(nba_team_data_test_lda_predicted)) {
  if(nba_team_data_test_fit$posterior[i, 1] < nba_team_data_test_fit$posterior[i, 2]) {
    nba_team_data_test_lda_predicted[i] = 1
  }
}

lda_fit_diagnostic <- nba_team_data_test_lda_predicted - as.numeric(nba_team_data_test$Playoffs)

prob_correct <- length(lda_fit_diagnostic[lda_fit_diagnostic == 0]) / length(lda_fit_diagnostic)

current_team_lda <- predict(lda_fit, current_team_data)

current_team_data$Playoff_Pred <- rep(0, nrow(current_team_data))

for(i in 1:nrow(current_team_data)) {
  if(current_team_lda$posterior[i, 1] < current_team_lda$posterior[i, 2]) {
    current_team_data[i, "Playoff_Pred"] = 1
  }
}

subset(current_team_data, select = c("Team", "Playoff_Pred"))


confus <- cbind(Actual = nba_team_data_test$Playoffs, Predicted = nba_team_data_test_fit$class)

confus <- as.data.frame(confus)

confus$Predicted = as.numeric(confus$Predicted)

confus <- mutate(confus, Predicted = Predicted - 1)

n1M <- subset(confus, Actual == 0)
n1M <- subset(n1M, Predicted == 1)
n1M <- nrow(n1M)

n2M <- subset(confus, Actual == 1)
n2M <- subset(n2M, Predicted == 0)
n2M <- nrow(n2M)

denom <- nrow(subset(confus, Actual == 0)) + nrow(subset(confus, Actual == 1))

aper <- (n1M + n2M) / denom

confusion(nba_team_data_test$Playoffs, nba_team_data_test_fit$class, prior = prior)

aper

# Future ideas
# Use cluster analysis to group playoff teams
# Compare these playoff results to current playoff seedings

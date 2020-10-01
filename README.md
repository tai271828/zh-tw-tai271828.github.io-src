# tai271828 zh blog based on pelican
## Repository management
- build by pelican
- branches
  - master - latest and stable codebase
  - master-draft - development branch of article drafts
  - dev - development branch of new features
  - dev-staging - rebased development branch of new features
  - staging - branch for staging site
  - published - branch for production site

## Work Flow
1. PREPARE Stage: merge master into dev and/or master-draft
1. DEVELOPMENT Stage: developing of new features (dev) and/or articles (master-draft)
1. TESTING Stage:
    1. the previous commits are rearranged as dev-staging and merged into the staging branch
    1. if the staging branch looks good after being published and reviewed by me or core readers, master will merge the staging branch.
1. PUBLISH Stage: publish master by creating the published branch
1. HOUSECLEANING Stage: replace dev with dev-staging and remove dev-staging

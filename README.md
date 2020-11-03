# tai271828 zh blog based on pelican
# Repository management
- build by pelican
- branches
  - master - latest and stable codebase
  - dev - development branch of new features and artiles including drafts. It might be overriden by force-push for rebasing if necessary.
  - staging - branch for staging site
  - published - branch for production site


# Work Flow
1. PREPARE Stage: merge master into dev
1. DEVELOPMENT Stage: developing of new features and/or articles on dev branch
1. TESTING Stage:
    1. the previous commits are rearranged and/or rebased and merged into the staging branch
    1. if the staging branch looks good after being published and reviewed by me or core readers, master will merge the staging branch.
1. PUBLISH Stage: publish master by creating the published branch
1. HOUSECLEANING Stage: remove cheap-dev- branches locally and remotely if necessary


# Convention
## prefix
cheap-dev- : usually used locally and an ephemeral branch with day-long life
dev- : a feature branch. may exist in the remote repository for days until the feature is complated or stop to work on the feature.


## Development and Maintenance Policy
In order to be easier to rebase later on, these policies are suggested:

- The following types of article should be commited one file always
    - drafts and articles in content folder
- The following types of article should be commited one file unless it is combined with feature update
    - README

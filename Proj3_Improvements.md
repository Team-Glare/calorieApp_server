## IMPROVEMENTS 

When our team took over the project from the previous group, we thoroughly reviewed the project in order to establish an effective takeover strategy. We attempted to improve the project in as many ways as possible. We've detailed the enhancements we've made in this document.

* Writing unit tests with proper mocking:
In Phase 2, there were unit tests written which had a code coverage of 56%. But the unit tests were calling the mongo server directly without mocking the network calls. In Phase 3, we have written proper unit tests using unittest and unittest-mock framework and have a code coverage of 98%. More information on the test cases can be found in the Software documentation file. 

* Deploying local mongo server to MongoAtlas:
We have deployed the local mongo server to MongoAtlas.

* Adding Linters, Code formatters in the CI pipeline:
In Phase 2, linter was added as a script that had to be run manually. We have added super-linter which encompasses both linter and code formatter and hooked into the Github actions CI pipeline.

* Improving Contributing.md:
We have added a template for the bug report (present in the docs file) and pull request in the Contributing. md.

* Adding Software Documentation:
We have added elaborate software documentation mentioning all the endpoint and test case details.

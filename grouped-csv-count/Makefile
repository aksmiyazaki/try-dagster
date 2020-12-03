.PHONY: test build

SBT_CLIENT := $(shell which sbt)

test:
	@$(SBT_CLIENT) clean coverage test coverageReport scapegoat

build:
	@$(SBT_CLIENT) assembly

Directory structure:
└── apify-apify-cli/
    ├── docs/
    │   ├── vars.md
    │   ├── integrating-scrapy.md
    │   ├── troubleshooting.md
    │   ├── reference.md
    │   ├── telemetry.md
    │   ├── index.md
    │   └── installation.md
    ├── tsconfig.typechecking.json
    ├── cucumber.json
    ├── CHANGELOG.md
    ├── .github/
    │   ├── scripts/
    │   │   └── before-beta-release.ts
    │   ├── workflows/
    │   │   ├── check.yaml
    │   │   ├── docs.yaml
    │   │   ├── cucumber.yaml
    │   │   ├── release.yaml
    │   │   ├── issue_labeling.yaml
    │   │   └── pre_release.yaml
    │   ├── hooks/
    │   │   └── pre-commit
    │   └── CODEOWNERS
    ├── renovate.json
    ├── tsconfig.eslint.json
    ├── biome.json
    ├── .eslintrc.json
    ├── test/
    │   ├── __setup__/
    │   │   ├── hooks/
    │   │   │   ├── useAuthSetup.ts
    │   │   │   ├── useProcessMock.ts
    │   │   │   ├── withRetries.ts
    │   │   │   ├── useConsoleSpy.ts
    │   │   │   └── useTempPath.ts
    │   │   ├── config.ts
    │   │   ├── build-utils.ts
    │   │   ├── test-data/
    │   │   │   └── input-file.json
    │   │   └── input-schemas/
    │   │       ├── prefills.json
    │   │       ├── missing-required-property.json
    │   │       ├── invalid.json
    │   │       ├── defaults.json
    │   │       ├── unparsable.json
    │   │       └── valid.json
    │   ├── crawlee/
    │   │   └── commands/
    │   │       └── run.test.ts
    │   ├── python_support.test.ts
    │   ├── lib/
    │   │   └── actor.test.ts
    │   ├── utils.test.ts
    │   ├── secrets.test.ts
    │   ├── consts.test.ts
    │   ├── tsconfig.json
    │   ├── version_check.test.ts
    │   ├── templates.test.ts
    │   └── commands/
    │       ├── create.test.ts
    │       ├── info.test.ts
    │       ├── validate-schema.test.ts
    │       ├── task/
    │       │   └── run.test.ts
    │       ├── call.test.ts
    │       ├── windows/
    │       │   └── create.test.ts
    │       ├── init.test.ts
    │       ├── secrets/
    │       │   ├── rm.test.ts
    │       │   └── add.test.ts
    │       ├── push.test.ts
    │       ├── pull.test.ts
    │       ├── log_in_out.test.ts
    │       └── run.test.ts
    ├── bin/
    │   ├── dev.cmd
    │   ├── dev.js
    │   ├── run.js
    │   ├── dev.sh
    │   └── run.cmd
    ├── .yarnrc.yml
    ├── package.json
    ├── .nvmrc
    ├── website/
    │   ├── sidebars.js
    │   ├── tsconfig.eslint.json
    │   ├── sitePlugin.js
    │   ├── .gitignore
    │   ├── .eslintrc.json
    │   ├── versions.json
    │   ├── .yarnrc.yml
    │   ├── tools/
    │   │   ├── docs-prettier.config.js
    │   │   └── utils/
    │   │       ├── createHref.js
    │   │       └── externalLink.js
    │   ├── package.json
    │   ├── versioned_docs/
    │   │   └── version-0.20/
    │   │       ├── vars.md
    │   │       ├── integrating-scrapy.md
    │   │       ├── troubleshooting.md
    │   │       ├── changelog.md
    │   │       ├── reference.md
    │   │       ├── telemetry.md
    │   │       ├── index.md
    │   │       └── installation.md
    │   ├── i18n/
    │   │   └── en/
    │   │       ├── docusaurus-theme-classic/
    │   │       │   ├── footer.json
    │   │       │   └── navbar.json
    │   │       ├── docusaurus-plugin-content-docs/
    │   │       │   ├── version-1.0.0.json
    │   │       │   ├── version-1.3.1.json
    │   │       │   ├── version-0.22.4.json
    │   │       │   ├── version-1.0.2.json
    │   │       │   ├── version-2.0.6.json
    │   │       │   ├── version-1.0.1.json
    │   │       │   ├── version-1.1.0.json
    │   │       │   ├── version-1.1.2.json
    │   │       │   ├── version-2.0.1.json
    │   │       │   ├── current.json
    │   │       │   └── version-1.2.0.json
    │   │       ├── docusaurus-plugin-content-blog/
    │   │       │   └── options.json
    │   │       └── code.json
    │   ├── yarn.lock
    │   ├── babel.config.js
    │   ├── versioned_sidebars/
    │   │   └── version-0.20-sidebars.json
    │   ├── docusaurus.config.js
    │   ├── src/
    │   │   ├── components/
    │   │   │   └── ApiLink.jsx
    │   │   └── pages/
    │   │       ├── index.module.css
    │   │       ├── versions.js
    │   │       └── index.js
    │   └── static/
    │       └── img/
    ├── vitest.config.ts
    ├── features/
    │   ├── builds-namespace.feature.md
    │   ├── invalid-actor-json-output.feature.md
    │   ├── actor-run-input.feature.md
    │   └── test-implementations/
    │       ├── 1.setup.ts
    │       ├── 0.utils.ts
    │       ├── 3.results.ts
    │       ├── 0.basic-actor.js
    │       ├── README.md
    │       ├── 2.execution.ts
    │       └── 0.world.ts
    ├── tsconfig.json
    ├── MIGRATIONS.md
    ├── README.md
    ├── CONTRIBUTING.md
    ├── src/
    │   ├── lib/
    │   │   ├── types.ts
    │   │   ├── exec.ts
    │   │   ├── telemetry.ts
    │   │   ├── version_check.ts
    │   │   ├── actor.ts
    │   │   ├── typings/
    │   │   │   ├── root-walk.d.ts
    │   │   │   ├── computer-name.d.ts
    │   │   │   └── tiged.d.ts
    │   │   ├── create-utils.ts
    │   │   ├── input_schema.ts
    │   │   ├── utils.ts
    │   │   ├── projects/
    │   │   │   ├── shared.ts
    │   │   │   ├── scrapy/
    │   │   │   │   ├── Spider.ts
    │   │   │   │   ├── SpiderFileAnalyzer.ts
    │   │   │   │   ├── wrapScrapyProject.ts
    │   │   │   │   └── ScrapyProjectAnalyzer.ts
    │   │   │   ├── CrawleeAnalyzer.ts
    │   │   │   └── OldApifySDKAnalyzer.ts
    │   │   ├── files.ts
    │   │   ├── apify_command.ts
    │   │   ├── secrets.ts
    │   │   ├── outputs.ts
    │   │   ├── consts.ts
    │   │   ├── community.ts
    │   │   ├── project_analyzer.ts
    │   │   ├── apify-oclif-help.ts
    │   │   ├── local_state.ts
    │   │   └── commands/
    │   │       ├── resolve-input.ts
    │   │       ├── responsive-table.ts
    │   │       ├── resolve-actor-context.ts
    │   │       ├── confirm.ts
    │   │       ├── pretty-print-status.ts
    │   │       ├── storages.ts
    │   │       ├── pretty-print-bytes.ts
    │   │       ├── run-on-cloud.ts
    │   │       └── read-stdin.ts
    │   ├── hooks/
    │   │   ├── init.ts
    │   │   └── deprecations.ts
    │   ├── index.ts
    │   └── commands/
    │       ├── runs/
    │       │   ├── ls.ts
    │       │   ├── info.ts
    │       │   ├── log.ts
    │       │   ├── index.ts
    │       │   ├── resurrect.ts
    │       │   ├── rm.ts
    │       │   └── abort.ts
    │       ├── run.ts
    │       ├── info.ts
    │       ├── pull.ts
    │       ├── task/
    │       │   ├── run.ts
    │       │   └── index.ts
    │       ├── push.ts
    │       ├── create.ts
    │       ├── init.ts
    │       ├── edit-input-schema.ts
    │       ├── request-queues/
    │       │   └── index.ts
    │       ├── key-value-stores/
    │       │   ├── ls.ts
    │       │   ├── get-value.ts
    │       │   ├── set-value.ts
    │       │   ├── delete-value.ts
    │       │   ├── create.ts
    │       │   ├── rename.ts
    │       │   ├── index.ts
    │       │   ├── keys.ts
    │       │   └── rm.ts
    │       ├── builds/
    │       │   ├── ls.ts
    │       │   ├── info.ts
    │       │   ├── log.ts
    │       │   ├── create.ts
    │       │   ├── index.ts
    │       │   └── rm.ts
    │       ├── login.ts
    │       ├── init-wrap-scrapy.ts
    │       ├── check-version.ts
    │       ├── validate-schema.ts
    │       ├── actor/
    │       │   ├── get-input.ts
    │       │   ├── get-value.ts
    │       │   ├── set-value.ts
    │       │   ├── index.ts
    │       │   └── push-data.ts
    │       ├── datasets/
    │       │   ├── ls.ts
    │       │   ├── get-items.ts
    │       │   ├── create.ts
    │       │   ├── rename.ts
    │       │   ├── index.ts
    │       │   ├── rm.ts
    │       │   └── push-items.ts
    │       ├── secrets/
    │       │   ├── index.ts
    │       │   ├── add.ts
    │       │   └── rm.ts
    │       ├── logout.ts
    │       ├── call.ts
    │       └── actors/
    │           ├── ls.ts
    │           ├── info.ts
    │           ├── start.ts
    │           ├── pull.ts
    │           ├── push.ts
    │           ├── build.ts
    │           ├── index.ts
    │           ├── rm.ts
    │           └── call.ts
    └── .editorconfig


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
File: /README.md
================================================
# Apify command-line interface (Apify CLI)

<a href="https://www.npmjs.com/package/apify-cli"><img src="https://badge.fury.io/js/apify-cli.svg" alt="npm version" loading="lazy" style="display:inherit;" /></a>
<a href="https://travis-ci.com/apify/apify-cli?branch=master"><img src="https://travis-ci.com/apify/apify-cli.svg?branch=master" loading="lazy" alt="Build Status" style="display:inherit;" /></a>

Apify command-line interface (Apify CLI) helps you create, develop, build and run
[Apify Actors](https://www.apify.com/actors),
and manage the Apify cloud platform from any computer.

Apify Actors are cloud programs that can perform arbitrary web scraping, automation or data processing job.
They accept input, perform their job and generate output.
While you can develop Actors in an online IDE directly in the [Apify web application](https://console.apify.com/),
for complex projects it is more convenient to develop Actors locally on your computer
using <a href="https://github.com/apify/apify-sdk-js">Apify SDK</a>
and only push the Actors to the Apify cloud during deployment.
This is where the Apify CLI comes in.

Note that Actors running on the Apify platform are executed in Docker containers, so with an appropriate `Dockerfile`
you can build your Actors in any programming language.
However, we recommend using JavaScript / Node.js, for which we provide most libraries and support.

## Installation

### Via Homebrew

On macOS (or Linux), you can install the Apify CLI via the [Homebrew package manager](https://brew.sh).

```bash
brew install apify-cli
```

### Via NPM

First, make sure you have [Node.js](https://nodejs.org) version 16 or higher with NPM installed on your computer:

```bash
node --version
npm --version
```

Install or upgrade Apify CLI by running:

```bash
npm -g install apify-cli
```

If you receive an `EACCES` error, you might need to run the command as root:

```bash
sudo npm -g install apify-cli
```

Alternatively, you can use [Node Version Manager (nvm)](https://github.com/nvm-sh/nvm) and install Apify CLI only into a selected user-level Node version without requiring root privileges:

```
nvm install 16
nvm use 16
npm -g install apify-cli
```

Finally, verify that Apify CLI was installed correctly by running:

```bash
apify --version
```

which should print something like:

```
apify-cli/0.10.0 darwin-x64 node-v16.14.2
```

> You can also skip the manual global installation altogether and use `npx apify-cli` with all the following commands instead.

## Basic usage

The following examples demonstrate the basic usage of Apify CLI.

### Create a new Actor from scratch

```bash
apify create my-hello-world
```

First, you will be prompted to select a template with the boilerplate for the Actor, to help you get started quickly.
The command will create a directory called `my-hello-world` that contains a Node.js project
for the Actor and a few configuration files.

> If you decided to skip the installation and go with `npx`, the command will be `npx apify-cli create my-hello-world`.

### Create a new Actor from existing project

```bash
cd ./my/awesome/project
apify init
```

This command will only set up local Actor development environment in an existing directory,
i.e. it will create the `.actor/actor.json` file and `apify_storage` directory.

Before you can run your project locally using `apify run`, you have to set up the right start command in `package.json` under scripts.start. For example:

```text
{
    ...
    "scripts": {
        "start": "node your_main_file.js",
    },
    ...
}
```

You can find more information about by running `apify help run`.

### Create a new Actor from Scrapy project

If you want to run a Scrapy project on Apify platform, follow the Scrapy integration guide [here](https://docs.apify.com/cli/docs/integrating-scrapy).

### Run the Actor locally

```bash
cd my-hello-world
apify run
```

This command runs the Actor on your local machine.
Now's your chance to develop the logic - or magic :smirk:

### Login with your Apify account

```bash
apify login
```

Before you can interact with the Apify cloud, you need to [create an Apify account](https://console.apify.com/)
and log in to it using the above command. You will be prompted for
your [Apify API token](https://console.apify.com/settings/integrations).
Note that the command will store the API token and other sensitive information to `~/.apify`.

### Push the Actor to the Apify cloud

```bash
apify push
```

This command uploads your project to the Apify cloud and builds an Actor from it. On the platform, Actor needs to be built before it can be run.

### Run an Actor on the Apify cloud

```bash
apify call
```

Runs the Actor corresponding to the current directory on the Apify platform.

This command can also be used to run other Actors, for example:

```bash
apify call apify/hello-world
```

### So what's in this .actor/actor.json file?

This file associates your local development project with an Actor on the Apify platform.
It contains information such as Actor name, version, build tag and environment variables.
Make sure you commit this file to the Git repository.

For example, `.actor/actor.json` file can look as follows:

```json
{
  "actorSpecification": 1,
  "name": "name-of-my-scraper",
  "version": "0.0",
  "buildTag": "latest",
  "environmentVariables": {
    "MYSQL_USER": "my_username",
    "MYSQL_PASSWORD": "@mySecretPassword"
  },
  "dockerfile": "./Dockerfile",
  "readme": "./ACTOR.md",
  "input": "./input_schema.json",
  "storages": {
    "dataset": "./dataset_schema.json"
  }
}
```

**`Dockerfile` field**\
If you specify the path to your Docker file under the `dockerfile` field, this file will be used for Actor builds on the platform. If not specified, the system will look for Docker files at `.actor/Dockerfile` and `Dockerfile` in this order of preference.

**`Readme` field** \
If you specify the path to your readme file under the `readme` field, the readme at this path will be used on the platform. If not specified, readme at `.actor/README.md` and `README.md` will be used in this order of preference.

**`Input` field**\
You can embed your [input schema](https://docs.apify.com/actors/development/input-schema#specification-version-1) object directly in `actor.json` under `input` field. Alternatively, you can provide a path to a custom input schema. If not provided, the input schema at `.actor/INPUT_SCHEMA.json` and `INPUT_SCHEMA.json` is used in this order of preference.

**`Storages.dataset` field**\
You can define the schema of the items in your dataset under the `storages.dataset` field. This can be either an embedded object or a path to a JSON schema file. You can read more about the schema of your Actor output [here](https://docs.apify.com/actors/development/output-schema#specification-version-1).

**Note on migration from deprecated config "apify.json"**\
_Note that previously, Actor config was stored in the `apify.json` file that has been deprecated. You can find the (very slight) differences and migration info in [migration guidelines](https://github.com/apify/apify-cli/blob/master/MIGRATIONS.md)._

## Environment variables

There are two options how you can set up environment variables for Actors.

### Set up environment variables in .actor/actor.json

All keys from `env` will be set as environment variables into Apify platform after you push Actor to Apify. Current values on Apify will be overridden.

```json
{
  "actorSpecification": 1,
  "name": "dataset-to-mysql",
  "version": "0.1",
  "buildTag": "latest",
  "environmentVariables": {
    "MYSQL_USER": "my_username",
    "MYSQL_PASSWORD": "@mySecretPassword"
  }
}
```

### Set up environment variables in Apify Console

In [Apify Console](https://console.apify.com/actors) select your Actor, you can set up variables into Source tab.
After setting up variables in the app, remove the `environmentVariables` from `.actor/actor.json`. Otherwise, variables from `.actor/actor.json` will override variables in the app.

```json
{
  "actorSpecification": 1,
  "name": "dataset-to-mysql",
  "version": "0.1",
  "buildTag": "latest"
}
```

#### How to set secret environment variables in .actor/actor.json

CLI provides commands to manage secrets environment variables. Secrets are stored to the `~/.apify` directory.
You can add a new secret using the command:

```bash
apify secrets:add mySecretPassword pwd1234
```

After adding a new secret you can use the secret in `.actor/actor.json`.

```text
{
    "actorSpecification": 1,
    "name": "dataset-to-mysql",
    ...
    "environmentVariables": {
      "MYSQL_PASSWORD": "@mySecretPassword"
    },
    ...
}
```

### Need help?

To see all CLI commands simply run:

```bash
apify help
```

To get information about a specific command run:

```bash
apify help COMMAND
```

Still haven't found what you were looking for? Please go to [Apify Help center](https://www.apify.com/help)
or [contact us](https://www.apify.com/contact).

## Command reference

This section contains printouts of `apify help` for all commands.

<!-- prettier-ignore-start -->
<!-- commands -->
* [`apify actor`](#apify-actor)
* [`apify actor get-input`](#apify-actor-get-input)
* [`apify actor get-value KEY`](#apify-actor-get-value-key)
* [`apify actor push-data [ITEM]`](#apify-actor-push-data-item)
* [`apify actor set-value KEY [VALUE]`](#apify-actor-set-value-key-value)
* [`apify actors`](#apify-actors)
* [`apify call [ACTORID]`](#apify-call-actorid)
* [`apify create [ACTORNAME]`](#apify-create-actorname)
* [`apify datasets`](#apify-datasets)
* [`apify help [COMMAND]`](#apify-help-command)
* [`apify info`](#apify-info)
* [`apify init [ACTORNAME]`](#apify-init-actorname)
* [`apify key-value-stores`](#apify-key-value-stores)
* [`apify login`](#apify-login)
* [`apify logout`](#apify-logout)
* [`apify pull [ACTORID]`](#apify-pull-actorid)
* [`apify push [ACTORID]`](#apify-push-actorid)
* [`apify request-queues`](#apify-request-queues)
* [`apify run`](#apify-run)
* [`apify runs`](#apify-runs)
* [`apify secrets`](#apify-secrets)
* [`apify secrets add NAME VALUE`](#apify-secrets-add-name-value)
* [`apify secrets rm NAME`](#apify-secrets-rm-name)
* [`apify task`](#apify-task)
* [`apify task run TASKID`](#apify-task-run-taskid)
* [`apify validate-schema [PATH]`](#apify-validate-schema-path)

## `apify actor`

Commands are designed to be used in Actor runs. All commands are in PoC state, do not use in production environments.

```
USAGE
  $ apify actor

DESCRIPTION
  Commands are designed to be used in Actor runs. All commands are in PoC state, do not use in production environments.
```

_See code: [src/commands/actor/index.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/actor/index.ts)_

## `apify actor get-input`

Gets the Actor input value from the default key-value store associated with the Actor run.

```
USAGE
  $ apify actor get-input

DESCRIPTION
  Gets the Actor input value from the default key-value store associated with the Actor run.
```

_See code: [src/commands/actor/get-input.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/actor/get-input.ts)_

## `apify actor get-value KEY`

Gets a value from the default key-value store associated with the Actor run.

```
USAGE
  $ apify actor get-value KEY

ARGUMENTS
  KEY  Key of the record in key-value store

DESCRIPTION
  Gets a value from the default key-value store associated with the Actor run.
```

_See code: [src/commands/actor/get-value.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/actor/get-value.ts)_

## `apify actor push-data [ITEM]`

Stores an object or an array of objects to the default dataset of the Actor run.

```
USAGE
  $ apify actor push-data [ITEM]

ARGUMENTS
  ITEM  JSON string with one object or array of objects containing data to be stored in the default dataset.

DESCRIPTION
  Stores an object or an array of objects to the default dataset of the Actor run.
  It is possible to pass data using item argument or stdin.
  Passing data using argument:
  $ apify actor push-data {"foo": "bar"}
  Passing data using stdin with pipe:
  $ cat ./test.json | apify actor push-data
```

_See code: [src/commands/actor/push-data.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/actor/push-data.ts)_

## `apify actor set-value KEY [VALUE]`

Sets or removes record into the default KeyValueStore associated with the Actor run.

```
USAGE
  $ apify actor set-value KEY [VALUE] [-c <value>]

ARGUMENTS
  KEY    Key of the record in key-value store.
  VALUE  Record data, which can be one of the following values:
         - If empty, the record in the key-value store is deleted.
         - If no `contentType` flag is specified, value is expected to be any JSON string value.
         - If options.contentType is set, value is taken as is.

FLAGS
  -c, --contentType=<value>  Specifies a custom MIME content type of the record. By default "application/json" is used.

DESCRIPTION
  Sets or removes record into the default KeyValueStore associated with the Actor run.
  It is possible to pass data using argument or stdin.
  Passing data using argument:
  $ apify actor set-value KEY my-value
  Passing data using stdin with pipe:
  $ cat ./my-text-file.txt | apify actor set-value KEY --contentType text/plain
```

_See code: [src/commands/actor/set-value.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/actor/set-value.ts)_

## `apify actors`

Commands are designed to be used with Actors.

```
USAGE
  $ apify actors

DESCRIPTION
  Commands are designed to be used with Actors.
```

_See code: [src/commands/actors/index.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/actors/index.ts)_

## `apify call [ACTORID]`

Runs a specific Actor remotely on the Apify cloud platform.

```
USAGE
  $ apify call [ACTORID] [-b <value>] [-t <value>] [-m <value>] [-w <value>] [-i <value> | --input-file
    <value>] [-s] [-o]

ARGUMENTS
  ACTORID  Name or ID of the Actor to run (e.g. "my-actor", "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not
           provided, the command runs the remote Actor specified in the ".actor/actor.json" file.

FLAGS
  -b, --build=<value>            Tag or number of the build to run (e.g. "latest" or "1.2.34").
  -i, --input=<value>            Optional JSON input to be given to the Actor.
  -m, --memory=<value>           Amount of memory allocated for the Actor run, in megabytes.
  -o, --output-dataset           Prints out the entire default dataset on successful run of the Actor.
  -s, --silent                   Prevents printing the logs of the Actor run to the console.
  -t, --timeout=<value>          Timeout for the Actor run in seconds. Zero value means there is no timeout.
  -w, --wait-for-finish=<value>  Seconds for waiting to run to finish, if no value passed, it waits forever.
      --input-file=<value>       Optional path to a file with JSON input to be given to the Actor. The file must be a
                                 valid JSON file. You can also specify `-` to read from standard input.

DESCRIPTION
  Runs a specific Actor remotely on the Apify cloud platform.
  The Actor is run under your current Apify account. Therefore you need to be logged in by calling "apify login". It
  takes input for the Actor from the default local key-value store by default.
```

_See code: [src/commands/call.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/call.ts)_

## `apify create [ACTORNAME]`

Creates a new Actor project directory from a selected boilerplate template.

```
USAGE
  $ apify create [ACTORNAME] [-t <value>] [--skip-dependency-install] [--omit-optional-deps]

ARGUMENTS
  ACTORNAME  Name of the Actor and its directory

FLAGS
  -t, --template=<value>         Template for the Actor. If not provided, the command will prompt for it.
                                 Visit
                                 https://raw.githubusercontent.com/apify/actor-templates/master/templates/manifest.json
                                 to find available template names.
      --omit-optional-deps       Skip installing optional dependencies.
      --skip-dependency-install  Skip installing Actor dependencies.

DESCRIPTION
  Creates a new Actor project directory from a selected boilerplate template.
```

_See code: [src/commands/create.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/create.ts)_

## `apify datasets`

Commands are designed to be used with Datasets.

```
USAGE
  $ apify datasets

DESCRIPTION
  Commands are designed to be used with Datasets.
```

_See code: [src/commands/datasets/index.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/datasets/index.ts)_

## `apify help [COMMAND]`

Display help for apify.

```
USAGE
  $ apify help [COMMAND...] [-n]

ARGUMENTS
  COMMAND...  Command to show help for.

FLAGS
  -n, --nested-commands  Include all nested commands in the output.

DESCRIPTION
  Display help for apify.
```

_See code: [@oclif/plugin-help](https://github.com/oclif/plugin-help/blob/v6.2.10/src/commands/help.ts)_

## `apify info`

Displays information about the currently active Apify account.

```
USAGE
  $ apify info

DESCRIPTION
  Displays information about the currently active Apify account.
  The information is printed to the console.
```

_See code: [src/commands/info.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/info.ts)_

## `apify init [ACTORNAME]`

Initializes a new Actor project in an existing directory.

```
USAGE
  $ apify init [ACTORNAME] [-y]

ARGUMENTS
  ACTORNAME  Name of the Actor. If not provided, you will be prompted for it.

FLAGS
  -y, --yes  Automatic yes to prompts; assume "yes" as answer to all prompts. Note that in some cases, the command may
             still ask for confirmation.

DESCRIPTION
  Initializes a new Actor project in an existing directory.
  If the directory contains a Scrapy project in Python, the command automatically creates wrappers so that you can run
  your scrapers without changes.

  The command creates the ".actor/actor.json" file and the "storage" directory in the current directory, but does not
  touch any other existing files or directories.

  WARNING: The directory at "storage" will be overwritten if it already exists.
```

_See code: [src/commands/init.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/init.ts)_

## `apify key-value-stores`

Commands are designed to be used with Key Value Stores.

```
USAGE
  $ apify key-value-stores

DESCRIPTION
  Commands are designed to be used with Key Value Stores.
```

_See code: [src/commands/key-value-stores/index.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/key-value-stores/index.ts)_

## `apify login`

Logs in to your Apify account.

```
USAGE
  $ apify login [-t <value>] [-m console|manual]

FLAGS
  -m, --method=<option>  [Optional] Method of logging in to Apify
                         <options: console|manual>
  -t, --token=<value>    [Optional] Apify API token

DESCRIPTION
  Logs in to your Apify account.
  The API token and other account information is stored in the ~/.apify directory, from where it is read by all other
  "apify" commands. To log out, call "apify logout".
```

_See code: [src/commands/login.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/login.ts)_

## `apify logout`

Logs out of your Apify account.

```
USAGE
  $ apify logout

DESCRIPTION
  Logs out of your Apify account.
  The command deletes the API token and all other account information stored in the ~/.apify directory. To log in again,
  call "apify login".
```

_See code: [src/commands/logout.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/logout.ts)_

## `apify pull [ACTORID]`

Pulls an Actor from the Apify platform to the current directory. If it is defined as Git repository, it will be cloned. If it is defined as Web IDE, it will fetch the files.

```
USAGE
  $ apify pull [ACTORID] [-v <value>]

ARGUMENTS
  ACTORID  Name or ID of the Actor to run (e.g. "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not provided, the
           command will update the Actor in the current directory based on its name in ".actor/actor.json" file.

FLAGS
  -v, --version=<value>  Actor version number which will be pulled, e.g. 1.2. Default: the highest version

DESCRIPTION
  Pulls an Actor from the Apify platform to the current directory. If it is defined as Git repository, it will be
  cloned. If it is defined as Web IDE, it will fetch the files.
```

_See code: [src/commands/pull.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/pull.ts)_

## `apify push [ACTORID]`

Uploads the Actor to the Apify platform and builds it there.

```
USAGE
  $ apify push [ACTORID] [--version-number <value>] [-v <value>] [-b <value>] [-w <value>] [--no-prompt]
    [--force]

ARGUMENTS
  ACTORID  Name or ID of the Actor to push (e.g. "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not provided, the
           command will create or modify the Actor with the name specified in ".actor/actor.json" file.

FLAGS
  -b, --build-tag=<value>        Build tag to be applied to the successful Actor build. By default, it is taken from the
                                 ".actor/actor.json" file
  -v, --version=<value>          Actor version number to which the files should be pushed. By default, it is taken from
                                 the ".actor/actor.json" file.
  -w, --wait-for-finish=<value>  Seconds for waiting to build to finish, if no value passed, it waits forever.
      --force                    Push an Actor even when the local files are older than the Actor on the platform.
      --no-prompt                Do not prompt for opening the Actor details in a browser. This will also not open the
                                 browser automatically.
      --version-number=<value>   DEPRECATED: Use flag version instead. Actor version number to which the files should be
                                 pushed. By default, it is taken from the ".actor/actor.json" file.

DESCRIPTION
  Uploads the Actor to the Apify platform and builds it there.
  The Actor settings are read from the ".actor/actor.json" file in the current directory, but they can be overridden
  using command-line options.
  NOTE: If the source files are smaller than 3 MB then they are uploaded as
  "Multiple source files", otherwise they are uploaded as "Zip file".

  When there's an attempt to push files that are older than the Actor on the platform, the command will fail. Can be
  overwritten with --force flag.
```

_See code: [src/commands/push.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/push.ts)_

## `apify request-queues`

Commands are designed to be used with Request Queues.

```
USAGE
  $ apify request-queues

DESCRIPTION
  Commands are designed to be used with Request Queues.
```

_See code: [src/commands/request-queues/index.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/request-queues/index.ts)_

## `apify run`

Runs the Actor locally in the current directory.

```
USAGE
  $ apify run [-p] [--purge-queue] [--purge-dataset] [--purge-key-value-store] [--entrypoint <value>] [-i
    <value> | --input-file <value>]

FLAGS
  -i, --input=<value>          Optional JSON input to be given to the Actor.
  -p, --purge                  Shortcut that combines the --purge-queue, --purge-dataset and --purge-key-value-store
                               options.
      --entrypoint=<value>     Optional entrypoint for running with injected environment variables.
                               For Python, it is the module name, or a path to a file.
                               For node.js, it is the npm script name, or a path to a JS/MJS file. You can also pass in
                               a directory name, provided that directory contains an "index.js" file.
      --input-file=<value>     Optional path to a file with JSON input to be given to the Actor. The file must be a
                               valid JSON file. You can also specify `-` to read from standard input.
      --purge-dataset          Deletes the local directory containing the default dataset before the run starts.
      --purge-key-value-store  Deletes all records from the default key-value store in the local directory before the
                               run starts, except for the "INPUT" key.
      --purge-queue            Deletes the local directory containing the default request queue before the run starts.

DESCRIPTION
  Runs the Actor locally in the current directory.
  It sets various APIFY_XYZ environment variables in order to provide a working execution environment for the Actor. For
  example, this causes the Actor input, as well as all other data in key-value stores, datasets or request queues to be
  stored in the "storage" directory, rather than on the Apify platform.

  NOTE: You can override the command's default behavior for Node.js Actors by overriding the "start" script in the
  package.json file. You can set up your own main file or environment variables by changing it.
```

_See code: [src/commands/run.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/run.ts)_

## `apify runs`

Commands are designed to be used with Actor Runs.

```
USAGE
  $ apify runs

DESCRIPTION
  Commands are designed to be used with Actor Runs.
```

_See code: [src/commands/runs/index.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/runs/index.ts)_

## `apify secrets`

Manages secret values for Actor environment variables.

```
USAGE
  $ apify secrets

DESCRIPTION
  Manages secret values for Actor environment variables.

  Example:
  $ apify secrets add mySecret TopSecretValue123

  Now the "mySecret" value can be used in an environment variable defined in ".actor/actor.json" file by adding the "@"
  prefix:

  {
  "actorSpecification": 1,
  "name": "my_actor",
  "environmentVariables": { "SECRET_ENV_VAR": "@mySecret" },
  "version": "0.1
  }

  When the Actor is pushed to Apify cloud, the "SECRET_ENV_VAR" and its value is stored as a secret environment variable
  of the Actor.
```

_See code: [src/commands/secrets/index.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/secrets/index.ts)_

## `apify secrets add NAME VALUE`

Adds a new secret value.

```
USAGE
  $ apify secrets add NAME VALUE

ARGUMENTS
  NAME   Name of the secret
  VALUE  Value of the secret

DESCRIPTION
  Adds a new secret value.
  The secrets are stored to a file at ~/.apify
```

_See code: [src/commands/secrets/add.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/secrets/add.ts)_

## `apify secrets rm NAME`

Removes the secret.

```
USAGE
  $ apify secrets rm NAME

ARGUMENTS
  NAME  Name of the secret

DESCRIPTION
  Removes the secret.
```

_See code: [src/commands/secrets/rm.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/secrets/rm.ts)_

## `apify task`

Commands are designed to be used to interact with Tasks.

```
USAGE
  $ apify task

DESCRIPTION
  Commands are designed to be used to interact with Tasks.
```

_See code: [src/commands/task/index.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/task/index.ts)_

## `apify task run TASKID`

Runs a specific Actor remotely on the Apify cloud platform.

```
USAGE
  $ apify task run TASKID [-b <value>] [-t <value>] [-m <value>] [-w <value>]

ARGUMENTS
  TASKID  Name or ID of the Task to run (e.g. "my-task" or "E2jjCZBezvAZnX8Rb").

FLAGS
  -b, --build=<value>            Tag or number of the build to run (e.g. "latest" or "1.2.34").
  -m, --memory=<value>           Amount of memory allocated for the Task run, in megabytes.
  -t, --timeout=<value>          Timeout for the Task run in seconds. Zero value means there is no timeout.
  -w, --wait-for-finish=<value>  Seconds for waiting to run to finish, if no value passed, it waits forever.

DESCRIPTION
  Runs a specific Actor remotely on the Apify cloud platform.
  The Actor is run under your current Apify account. Therefore you need to be logged in by calling "apify login". It
  takes input for the Actor from the default local key-value store by default.
```

_See code: [src/commands/task/run.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/task/run.ts)_

## `apify validate-schema [PATH]`

Validates input schema and prints errors found.

```
USAGE
  $ apify validate-schema [PATH]

ARGUMENTS
  PATH  Optional path to your INPUT_SCHEMA.json file. If not provided ./INPUT_SCHEMA.json is used.

DESCRIPTION
  Validates input schema and prints errors found.
  The input schema for the Actor is used from these locations in order of preference.
  The first one found is validated as it would be the one used on the Apify platform.
  1. Directly embedded object in ".actor/actor.json" under 'input' key
  2. Path to JSON file referenced in ".actor/actor.json" under 'input' key
  3. JSON file at .actor/INPUT_SCHEMA.json
  4. JSON file at INPUT_SCHEMA.json

  You can also pass any custom path to your input schema to have it validated instead.
```

_See code: [src/commands/validate-schema.ts](https://github.com/apify/apify-cli/blob/v0.20.7/src/commands/validate-schema.ts)_
<!-- commandsstop -->
<!-- prettier-ignore-end -->


================================================
File: /docs/vars.md
================================================
---
sidebar_label: Environment variables
title: Environment variables
---

There are two options how you can set up environment variables for Actors.

### Set up environment variables in `.actor/actor.json`

All keys from `env` will be set as environment variables into Apify platform after you push Actor to Apify. Current values on Apify will be overridden.

```json
{
  "actorSpecification": 1,
  "name": "dataset-to-mysql",
  "version": "0.1",
  "buildTag": "latest",
  "environmentVariables": {
    "MYSQL_USER": "my_username",
    "MYSQL_PASSWORD": "@mySecretPassword"
  }
}
```

### Set up environment variables in Apify Console

In [Apify Console](https://console.apify.com/actors) select your Actor, you can set up variables into Source tab.
After setting up variables in the app, remove the `environmentVariables` from `.actor/actor.json`. Otherwise, variables from `.actor/actor.json` will override variables in the app.

```json
{
  "actorSpecification": 1,
  "name": "dataset-to-mysql",
  "version": "0.1",
  "buildTag": "latest"
}
```

#### How to set secret environment variables in `.actor/actor.json`

CLI provides commands to manage secrets environment variables. Secrets are stored to the `~/.apify` directory.
You can add a new secret using the command:

```bash
apify secrets add mySecretPassword pwd1234
```

After adding a new secret you can use the secret in `.actor/actor.json`.

```text
{
    "actorSpecification": 1,
    "name": "dataset-to-mysql",
    ...
    "environmentVariables": {
      "MYSQL_PASSWORD": "@mySecretPassword"
    },
    ...
}
```

### Need help?

To see all CLI commands simply run:

```bash
apify help
```

To get information about a specific command run:

```bash
apify help COMMAND
```

Still haven't found what you were looking for? Please go to [Apify Help center](https://www.apify.com/help)
or [contact us](https://www.apify.com/contact).


================================================
File: /docs/integrating-scrapy.md
================================================
---
title: Integrating Scrapy projects
description: Learn how to run Scrapy projects as Apify Actors and deploy them on the Apify platform.
sidebar_label: Integrating Scrapy projects
---

[Scrapy](https://scrapy.org/) is a widely used open-source web scraping framework for Python. Scrapy projects can now be executed on the Apify platform using our dedicated wrapping tool. This tool allows users to transform their Scrapy projects into [Apify Actors](https://docs.apify.com/platform/actors) with just a few simple commands.

## Getting started

### Install Apify CLI

To run the migration tool, you need to have the Apify CLI installed. You can install it using Homebrew with the following command:

```bash showLineNumbers
brew install apify-cli
```

Alternatively, you can install it using NPM with the following command:

```bash showLineNumbers
npm i -g apify-cli
```

In case of any issues, please refer to the [installation guide](./installation.md).

## Actorization of your existing Scrapy spider

Assuming your Scrapy project is set up, navigate to the project root where the `scrapy.cfg` file is located.

```bash showLineNumbers
cd your_scraper
```

Verify the directory contents to ensure the correct location.

```bash showLineNumbers
$ ls -R
.:
your_scraper  README.md  requirements.txt  scrapy.cfg

./your_scraper:
__init__.py  items.py  __main__.py  main.py  pipelines.py  settings.py  spiders

./your_scraper/spiders:
your_spider.py  __init__.py
```

To convert your Scrapy project into an Apify Actor, initiate the wrapping process by executing the following command:

```bash showLineNumbers
apify init
```

The script will prompt you with a series of questions. Upon completion, the output might resemble the following:

```bash showLineNumbers
Info: The current directory looks like a Scrapy project. Using automatic project wrapping.
? Enter the Scrapy BOT_NAME (see settings.py): books_scraper
? What folder are the Scrapy spider modules stored in? (see SPIDER_MODULES in settings.py): books_scraper.spiders
? Pick the Scrapy spider you want to wrap: BookSpider (/home/path/to/actor-scrapy-books-example/books_scraper/spiders/book.py)
Info: Downloading the latest Scrapy wrapper template...
Info: Wrapping the Scrapy project...
Success: The Scrapy project has been wrapped successfully.
```

For example, here is a [source code](https://github.com/apify/actor-scrapy-books-example) of an actorized Scrapy project, and [here](https://apify.com/vdusek/scrapy-books-example) the corresponding Actor in Apify Store.

### Run the Actor locally

Create a Python virtual environment by running:

```bash showLineNumbers
python -m virtualenv .venv
```

Activate the virtual environment:

```bash showLineNumbers
source .venv/bin/activate
```

Install Python dependencies using the provided requirements file named `requirements_apify.txt`. Ensure these requirements are installed before executing your project as an Apify Actor locally. You can put your own dependencies there as well.

```bash showLineNumbers
pip install -r requirements-apify.txt [-r requirements.txt]
```

Finally execute the Apify Actor.

```bash showLineNumbers
apify run [--purge]
```

If [ActorDatasetPushPipeline](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/pipelines.py) is configured, the Actor's output will be stored in the `storage/datasets/default/` directory.

### Run the scraper as Scrapy project

The project remains executable as a Scrapy project.

```bash showLineNumbers
scrapy crawl your_spider -o books.json
```

## Deploy on Apify

### Log in to Apify

You will need to provide your [Apify API Token](https://console.apify.com/settings/integrations) to complete this action.

```bash showLineNumbers
apify login
```

### Deploy your Actor

This command will deploy and build the Actor on the Apify platform. You can find your newly created Actor under [Actors -> My Actors](https://console.apify.com/actors?tab=my).

```bash showLineNumbers
apify push
```

## What the wrapping process does

The initialization command enhances your project by adding necessary files and updating some of them while preserving its functionality as a typical Scrapy project. The additional requirements file, named `requirements_apify.txt`, includes the Apify Python SDK and other essential requirements. The `.actor/` directory contains basic configuration of your Actor. We provide two new Python files [main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py) and [\_\_main\_\_.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/__main__.py), where we encapsulate the Scrapy project within an Actor. We also import and use there a few Scrapy components from our [Python SDK](https://github.com/apify/apify-sdk-python/tree/master/src/apify/scrapy). These components facilitate the integration of the Scrapy projects with the Apify platform. Further details about these components are provided in the following subsections.

### Scheduler

The [scheduler](https://docs.scrapy.org/en/latest/topics/scheduler.html) is a core component of Scrapy responsible for receiving and providing requests to be processed. To leverage the [Apify request queue](https://docs.apify.com/platform/storage/request-queue) for storing requests, a custom scheduler becomes necessary. Fortunately, Scrapy is a modular framework, allowing the creation of custom components. As a result, we have implemented the [ApifyScheduler](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/scheduler.py). When using the Apify CLI wrapping tool, the scheduler is configured in the [src/main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py) file of your Actor.

### Dataset push pipeline

[Item pipelines](https://docs.scrapy.org/en/latest/topics/item-pipeline.html) are used for the processing of the results produced by your spiders. To handle the transmission of result data to the [Apify dataset](https://docs.apify.com/platform/storage/dataset), we have implemented the [ActorDatasetPushPipeline](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/pipelines.py). When using the Apify CLI wrapping tool, the pipeline is configured in the [src/main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py) file of your Actor. It is assigned the highest integer value (1000), ensuring its execution as the final step in the pipeline sequence.

### Retry middleware

[Downloader middlewares](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html) are a way how to hook into Scrapy's request/response processing. Scrapy comes with various default middlewares, including the [RetryMiddleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#module-scrapy.downloadermiddlewares.retry), designed to handle retries for requests that may have failed due to temporary issues. When integrating with the [Apify request queue](https://docs.apify.com/platform/storage/request-queue), it becomes necessary to enhance this middleware to facilitate communication with the request queue marking the requests either as handled or ready for a retry. When using the Apify CLI wrapping tool, the default `RetryMiddleware` is disabled, and [ApifyRetryMiddleware](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/middlewares/apify_retry.py) takes its place. Configuration for the middlewares is established in the [src/main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py) file of your Actor.

### HTTP proxy middleware

Another default Scrapy [downloader middleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html) that requires replacement is [HttpProxyMiddleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#module-scrapy.downloadermiddlewares.httpproxy). To utilize the use of proxies managed through the Apify [ProxyConfiguration](https://github.com/apify/apify-sdk-python/blob/master/src/apify/proxy_configuration.py), we provide [ApifyHttpProxyMiddleware](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/middlewares/apify_proxy.py). When using the Apify CLI wrapping tool, the default `HttpProxyMiddleware` is disabled, and [ApifyHttpProxyMiddleware](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/middlewares/apify_proxy.py) takes its place. Additionally, inspect the [.actor/input_schema.json](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/.actor/input_schema.json) file, where proxy configuration is specified as an input property for your Actor. The processing of this input is carried out together with the middleware configuration in [src/main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py).

## Known limitations

There are some known limitations of running the Scrapy projects on Apify platform we are aware of.

### Asynchronous code in spiders and other components

Scrapy asynchronous execution is based on the [Twisted](https://twisted.org/) library, not the
[AsyncIO](https://docs.python.org/3/library/asyncio.html), which brings some complications on the table.

Due to the asynchronous nature of the Actors, all of their code is executed as a coroutine inside the `asyncio.run`.
In order to execute Scrapy code inside an Actor, following the section
[Run Scrapy from a script](https://docs.scrapy.org/en/latest/topics/practices.html?highlight=CrawlerProcess#run-scrapy-from-a-script)
from the official Scrapy documentation, we need to invoke a
[`CrawlProcess.start`](https://github.com/scrapy/scrapy/blob/2.11.0/scrapy/crawler.py#L393:L427)
method. This method triggers Twisted's event loop, also known as a reactor.
Consequently, Twisted's event loop is executed within AsyncIO's event loop.
On top of that, when employing AsyncIO code in spiders or other components, it necessitates the creation of a new
AsyncIO event loop, within which the coroutines from these components are executed. This means there is
an execution of the AsyncIO event loop inside the Twisted event loop inside the AsyncIO event loop.

We have resolved this issue by leveraging the [nest-asyncio](https://pypi.org/project/nest-asyncio/) library,
enabling the execution of nested AsyncIO event loops. For executing a coroutine within a spider or other component,
it is recommended to use Apify's instance of the nested event loop. Refer to the code example below or derive
inspiration from Apify's Scrapy components, such as the
[ApifyScheduler](https://github.com/apify/apify-sdk-python/blob/v1.5.0/src/apify/scrapy/scheduler.py#L114).

```python showLineNumbers
from apify.scrapy.utils import nested_event_loop

...

# Coroutine execution inside a spider
nested_event_loop.run_until_complete(my_coroutine())
```

### More spiders per Actor

It is recommended to execute only one Scrapy spider per Apify Actor.

Mapping more Scrapy spiders to a single Apify Actor does not make much sense. We would have to create a separate
instace of the [request queue](https://docs.apify.com/platform/storage/request-queue) for every spider.
Also, every spider can produce a different output resulting in a mess in an output
[dataset](https://docs.apify.com/platform/storage/dataset). A solution for this could be to store an output
of every spider to a different [key-value store](https://docs.apify.com/platform/storage/key-value-store). However,
a much more simple solution to this problem would be to just have a single spider per Actor.

If you want to share common Scrapy components (middlewares, item pipelines, ...) among more spiders (Actors), you
can use a dedicated Python package containing your components and install it to your Actors environment. The
other solution to this problem could be to have more spiders per Actor, but keep only one spider run per Actor.
What spider is going to be executed in an Actor run can be specified in the
[input schema](https://docs.apify.com/academy/deploying-your-code/input-schema).

## Additional links

- [Scrapy Books Example Actor](https://apify.com/vdusek/scrapy-books-example)
- [Python Actor Scrapy template](https://apify.com/templates/python-scrapy)
- [Apify SDK for Python](https://docs.apify.com/sdk/python)
- [Apify platform](https://docs.apify.com/platform)
- [Join our developer community on Discord](https://discord.com/invite/jyEM2PRvMU)

> We welcome any feedback! Please feel free to contact us at [python@apify.com](mailto:python@apify.com). Thank you for your valuable input.


================================================
File: /docs/troubleshooting.md
================================================
---
sidebar_label: Troubleshooting
title: Troubleshooting
---

For general support, reach out to us at [apify.com/contact](https://apify.com/contact).

If you believe you are encountering a bug, file it on [GitHub](https://github.com/apify/apify-cli/issues/new).


================================================
File: /docs/reference.md
================================================
---
title: Command reference
---

This section contains printouts of `apify help` for all commands.

<!-- prettier-ignore-start -->
<!-- commands -->
* [`apify actor`](#apify-actor)
* [`apify actor get-input`](#apify-actor-get-input)
* [`apify actor get-value KEY`](#apify-actor-get-value-key)
* [`apify actor push-data [ITEM]`](#apify-actor-push-data-item)
* [`apify actor set-value KEY [VALUE]`](#apify-actor-set-value-key-value)
* [`apify actors`](#apify-actors)
* [`apify actors build [ACTORID]`](#apify-actors-build-actorid)
* [`apify actors call [ACTORID]`](#apify-actors-call-actorid)
* [`apify actors ls`](#apify-actors-ls)
* [`apify actors pull [ACTORID]`](#apify-actors-pull-actorid)
* [`apify actors push [ACTORID]`](#apify-actors-push-actorid)
* [`apify actors rm ACTORID`](#apify-actors-rm-actorid)
* [`apify actors start [ACTORID]`](#apify-actors-start-actorid)
* [`apify builds`](#apify-builds)
* [`apify builds create [ACTORID]`](#apify-builds-create-actorid)
* [`apify builds info BUILDID`](#apify-builds-info-buildid)
* [`apify builds log BUILDID`](#apify-builds-log-buildid)
* [`apify builds ls [ACTORID]`](#apify-builds-ls-actorid)
* [`apify builds rm BUILDID`](#apify-builds-rm-buildid)
* [`apify call [ACTORID]`](#apify-call-actorid)
* [`apify create [ACTORNAME]`](#apify-create-actorname)
* [`apify datasets`](#apify-datasets)
* [`apify datasets create [DATASETNAME]`](#apify-datasets-create-datasetname)
* [`apify datasets get-items DATASETID`](#apify-datasets-get-items-datasetid)
* [`apify datasets ls`](#apify-datasets-ls)
* [`apify datasets push-items NAMEORID ITEM`](#apify-datasets-push-items-nameorid-item)
* [`apify datasets rename NAMEORID [NEWNAME]`](#apify-datasets-rename-nameorid-newname)
* [`apify datasets rm DATASETNAMEORID`](#apify-datasets-rm-datasetnameorid)
* [`apify help [COMMAND]`](#apify-help-command)
* [`apify info`](#apify-info)
* [`apify init [ACTORNAME]`](#apify-init-actorname)
* [`apify key-value-stores`](#apify-key-value-stores)
* [`apify key-value-stores create [KEYVALUESTORENAME]`](#apify-key-value-stores-create-keyvaluestorename)
* [`apify key-value-stores delete-value STOREID ITEMKEY`](#apify-key-value-stores-delete-value-storeid-itemkey)
* [`apify key-value-stores get-value KEYVALUESTOREID ITEMKEY`](#apify-key-value-stores-get-value-keyvaluestoreid-itemkey)
* [`apify key-value-stores keys STOREID`](#apify-key-value-stores-keys-storeid)
* [`apify key-value-stores ls`](#apify-key-value-stores-ls)
* [`apify key-value-stores rename KEYVALUESTORENAMEORID [NEWNAME]`](#apify-key-value-stores-rename-keyvaluestorenameorid-newname)
* [`apify key-value-stores rm KEYVALUESTORENAMEORID`](#apify-key-value-stores-rm-keyvaluestorenameorid)
* [`apify key-value-stores set-value STOREID ITEMKEY [VALUE]`](#apify-key-value-stores-set-value-storeid-itemkey-value)
* [`apify login`](#apify-login)
* [`apify logout`](#apify-logout)
* [`apify pull [ACTORID]`](#apify-pull-actorid)
* [`apify push [ACTORID]`](#apify-push-actorid)
* [`apify request-queues`](#apify-request-queues)
* [`apify run`](#apify-run)
* [`apify runs`](#apify-runs)
* [`apify runs abort RUNID`](#apify-runs-abort-runid)
* [`apify runs info RUNID`](#apify-runs-info-runid)
* [`apify runs log RUNID`](#apify-runs-log-runid)
* [`apify runs ls [ACTORID]`](#apify-runs-ls-actorid)
* [`apify runs resurrect RUNID`](#apify-runs-resurrect-runid)
* [`apify runs rm RUNID`](#apify-runs-rm-runid)
* [`apify secrets`](#apify-secrets)
* [`apify secrets add NAME VALUE`](#apify-secrets-add-name-value)
* [`apify secrets rm NAME`](#apify-secrets-rm-name)
* [`apify task`](#apify-task)
* [`apify task run TASKID`](#apify-task-run-taskid)
* [`apify validate-schema [PATH]`](#apify-validate-schema-path)

## `apify actor`

Commands are designed to be used in Actor runs. All commands are in PoC state, do not use in production environments.

```
USAGE
  $ apify actor

DESCRIPTION
  Commands are designed to be used in Actor runs. All commands are in PoC state, do not use in production environments.
```

_See code: [src/commands/actor/index.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actor/index.ts)_

## `apify actor get-input`

Gets the Actor input value from the default key-value store associated with the Actor run.

```
USAGE
  $ apify actor get-input

DESCRIPTION
  Gets the Actor input value from the default key-value store associated with the Actor run.
```

_See code: [src/commands/actor/get-input.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actor/get-input.ts)_

## `apify actor get-value KEY`

Gets a value from the default key-value store associated with the Actor run.

```
USAGE
  $ apify actor get-value KEY

ARGUMENTS
  KEY  Key of the record in key-value store

DESCRIPTION
  Gets a value from the default key-value store associated with the Actor run.
```

_See code: [src/commands/actor/get-value.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actor/get-value.ts)_

## `apify actor push-data [ITEM]`

Stores an object or an array of objects to the default dataset of the Actor run.

```
USAGE
  $ apify actor push-data [ITEM]

ARGUMENTS
  ITEM  JSON string with one object or array of objects containing data to be stored in the default dataset.

DESCRIPTION
  Stores an object or an array of objects to the default dataset of the Actor run.
  It is possible to pass data using item argument or stdin.
  Passing data using argument:
  $ apify actor push-data {"foo": "bar"}
  Passing data using stdin with pipe:
  $ cat ./test.json | apify actor push-data
```

_See code: [src/commands/actor/push-data.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actor/push-data.ts)_

## `apify actor set-value KEY [VALUE]`

Sets or removes record into the default KeyValueStore associated with the Actor run.

```
USAGE
  $ apify actor set-value KEY [VALUE] [-c <value>]

ARGUMENTS
  KEY    Key of the record in key-value store.
  VALUE  Record data, which can be one of the following values:
         - If empty, the record in the key-value store is deleted.
         - If no `contentType` flag is specified, value is expected to be any JSON string value.
         - If options.contentType is set, value is taken as is.

FLAGS
  -c, --contentType=<value>  Specifies a custom MIME content type of the record. By default "application/json" is used.

DESCRIPTION
  Sets or removes record into the default KeyValueStore associated with the Actor run.
  It is possible to pass data using argument or stdin.
  Passing data using argument:
  $ apify actor set-value KEY my-value
  Passing data using stdin with pipe:
  $ cat ./my-text-file.txt | apify actor set-value KEY --contentType text/plain
```

_See code: [src/commands/actor/set-value.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actor/set-value.ts)_

## `apify actors`

Commands are designed to be used with Actors.

```
USAGE
  $ apify actors

DESCRIPTION
  Commands are designed to be used with Actors.
```

_See code: [src/commands/actors/index.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actors/index.ts)_

## `apify actors build [ACTORID]`

Creates a new build of the Actor.

```
USAGE
  $ apify actors build [ACTORID] [--json] [--tag <value>] [--version <value>] [--log]

ARGUMENTS
  ACTORID  Optional Actor ID or Name to trigger a build for. By default, it will use the Actor from the current
           directory.

FLAGS
  --log              Whether to print out the build log after the build is triggered.
  --tag=<value>      Build tag to be applied to the successful Actor build. By default, this is "latest".
  --version=<value>  Optional Actor Version to build. By default, this will be inferred from the tag, but this flag is
                     required when multiple versions have the same tag.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Creates a new build of the Actor.
```

_See code: [src/commands/actors/build.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actors/build.ts)_

## `apify actors call [ACTORID]`

Runs a specific Actor remotely on the Apify cloud platform.

```
USAGE
  $ apify actors call [ACTORID] [--json] [-b <value>] [-t <value>] [-m <value>] [-i <value> | --input-file
    <value>] [-s] [-o]

ARGUMENTS
  ACTORID  Name or ID of the Actor to run (e.g. "my-actor", "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not
           provided, the command runs the remote Actor specified in the ".actor/actor.json" file.

FLAGS
  -b, --build=<value>       Tag or number of the build to run (e.g. "latest" or "1.2.34").
  -i, --input=<value>       Optional JSON input to be given to the Actor.
  -m, --memory=<value>      Amount of memory allocated for the Actor run, in megabytes.
  -o, --output-dataset      Prints out the entire default dataset on successful run of the Actor.
  -s, --silent              Prevents printing the logs of the Actor run to the console.
  -t, --timeout=<value>     Timeout for the Actor run in seconds. Zero value means there is no timeout.
      --input-file=<value>  Optional path to a file with JSON input to be given to the Actor. The file must be a valid
                            JSON file. You can also specify `-` to read from standard input.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Runs a specific Actor remotely on the Apify cloud platform.
  The Actor is run under your current Apify account. Therefore you need to be logged in by calling "apify login". It
  takes input for the Actor from the default local key-value store by default.
```

_See code: [src/commands/actors/call.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actors/call.ts)_

## `apify actors ls`

Lists all recently ran Actors or your own Actors.

```
USAGE
  $ apify actors ls [--json] [--my] [--offset <value>] [--limit <value>] [--desc]

FLAGS
  --desc            Sort Actors in descending order.
  --limit=<value>   [default: 20] Number of Actors that will be listed.
  --my              Whether to list Actors made by the logged in user.
  --offset=<value>  Number of Actors that will be skipped.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Lists all recently ran Actors or your own Actors.
```

_See code: [src/commands/actors/ls.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actors/ls.ts)_

## `apify actors pull [ACTORID]`

Pulls an Actor from the Apify platform to the current directory. If it is defined as Git repository, it will be cloned. If it is defined as Web IDE, it will fetch the files.

```
USAGE
  $ apify actors pull [ACTORID] [-v <value>] [--dir <value>]

ARGUMENTS
  ACTORID  Name or ID of the Actor to run (e.g. "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not provided, the
           command will update the Actor in the current directory based on its name in ".actor/actor.json" file.

FLAGS
  -v, --version=<value>  Actor version number which will be pulled, e.g. 1.2. Default: the highest version
      --dir=<value>      Directory where the Actor should be pulled to

DESCRIPTION
  Pulls an Actor from the Apify platform to the current directory. If it is defined as Git repository, it will be
  cloned. If it is defined as Web IDE, it will fetch the files.
```

_See code: [src/commands/actors/pull.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actors/pull.ts)_

## `apify actors push [ACTORID]`

Uploads the Actor to the Apify platform and builds it there.

```
USAGE
  $ apify actors push [ACTORID] [-v <value>] [-b <value>] [-w <value>] [--no-prompt] [--force] [--dir <value>]

ARGUMENTS
  ACTORID  Name or ID of the Actor to push (e.g. "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not provided, the
           command will create or modify the Actor with the name specified in ".actor/actor.json" file.

FLAGS
  -b, --build-tag=<value>        Build tag to be applied to the successful Actor build. By default, it is taken from the
                                 ".actor/actor.json" file
  -v, --version=<value>          Actor version number to which the files should be pushed. By default, it is taken from
                                 the ".actor/actor.json" file.
  -w, --wait-for-finish=<value>  Seconds for waiting to build to finish, if no value passed, it waits forever.
      --dir=<value>              Directory where the Actor is located
      --force                    Push an Actor even when the local files are older than the Actor on the platform.
      --no-prompt                Do not prompt for opening the Actor details in a browser. This will also not open the
                                 browser automatically.

DESCRIPTION
  Uploads the Actor to the Apify platform and builds it there.
  The Actor settings are read from the ".actor/actor.json" file in the current directory, but they can be overridden
  using command-line options.
  NOTE: If the source files are smaller than 3 MB then they are uploaded as
  "Multiple source files", otherwise they are uploaded as "Zip file".

  When there's an attempt to push files that are older than the Actor on the platform, the command will fail. Can be
  overwritten with --force flag.
```

_See code: [src/commands/actors/push.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actors/push.ts)_

## `apify actors rm ACTORID`

Deletes an Actor.

```
USAGE
  $ apify actors rm ACTORID

ARGUMENTS
  ACTORID  The Actor ID to delete.

DESCRIPTION
  Deletes an Actor.
```

_See code: [src/commands/actors/rm.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actors/rm.ts)_

## `apify actors start [ACTORID]`

Runs a specific Actor remotely on the Apify cloud platform and immediately returns information about the run.

```
USAGE
  $ apify actors start [ACTORID] [--json] [-b <value>] [-t <value>] [-m <value>] [-i <value> | --input-file
    <value>]

ARGUMENTS
  ACTORID  Name or ID of the Actor to run (e.g. "my-actor", "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not
           provided, the command runs the remote Actor specified in the ".actor/actor.json" file.

FLAGS
  -b, --build=<value>       Tag or number of the build to run (e.g. "latest" or "1.2.34").
  -i, --input=<value>       Optional JSON input to be given to the Actor.
  -m, --memory=<value>      Amount of memory allocated for the Actor run, in megabytes.
  -t, --timeout=<value>     Timeout for the Actor run in seconds. Zero value means there is no timeout.
      --input-file=<value>  Optional path to a file with JSON input to be given to the Actor. The file must be a valid
                            JSON file. You can also specify `-` to read from standard input.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Runs a specific Actor remotely on the Apify cloud platform and immediately returns information about the run.
  The Actor is run under your current Apify account. Therefore you need to be logged in by calling "apify login". It
  takes input for the Actor from the default local key-value store by default.
```

_See code: [src/commands/actors/start.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/actors/start.ts)_

## `apify builds`

Commands are designed to be used with Actor Builds.

```
USAGE
  $ apify builds

DESCRIPTION
  Commands are designed to be used with Actor Builds.
```

_See code: [src/commands/builds/index.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/builds/index.ts)_

## `apify builds create [ACTORID]`

Creates a new build of the Actor.

```
USAGE
  $ apify builds create [ACTORID] [--json] [--tag <value>] [--version <value>] [--log]

ARGUMENTS
  ACTORID  Optional Actor ID or Name to trigger a build for. By default, it will use the Actor from the current
           directory.

FLAGS
  --log              Whether to print out the build log after the build is triggered.
  --tag=<value>      Build tag to be applied to the successful Actor build. By default, this is "latest".
  --version=<value>  Optional Actor Version to build. By default, this will be inferred from the tag, but this flag is
                     required when multiple versions have the same tag.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Creates a new build of the Actor.
```

_See code: [src/commands/builds/create.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/builds/create.ts)_

## `apify builds info BUILDID`

Prints information about a specific build.

```
USAGE
  $ apify builds info BUILDID [--json]

ARGUMENTS
  BUILDID  The build ID to get information about.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Prints information about a specific build.
```

_See code: [src/commands/builds/info.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/builds/info.ts)_

## `apify builds log BUILDID`

Prints the log of a specific build.

```
USAGE
  $ apify builds log BUILDID

ARGUMENTS
  BUILDID  The build ID to get the log from.

DESCRIPTION
  Prints the log of a specific build.
```

_See code: [src/commands/builds/log.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/builds/log.ts)_

## `apify builds ls [ACTORID]`

Lists all builds of the Actor.

```
USAGE
  $ apify builds ls [ACTORID] [--json] [--offset <value>] [--limit <value>] [--desc] [-c]

ARGUMENTS
  ACTORID  Optional Actor ID or Name to list runs for. By default, it will use the Actor from the current directory.

FLAGS
  -c, --compact         Display a compact table.
      --desc            Sort builds in descending order.
      --limit=<value>   [default: 10] Number of builds that will be listed.
      --offset=<value>  Number of builds that will be skipped.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Lists all builds of the Actor.
```

_See code: [src/commands/builds/ls.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/builds/ls.ts)_

## `apify builds rm BUILDID`

Deletes an Actor Build.

```
USAGE
  $ apify builds rm BUILDID

ARGUMENTS
  BUILDID  The build ID to delete.

DESCRIPTION
  Deletes an Actor Build.
```

_See code: [src/commands/builds/rm.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/builds/rm.ts)_

## `apify call [ACTORID]`

Runs a specific Actor remotely on the Apify cloud platform.

```
USAGE
  $ apify call [ACTORID] [--json] [-b <value>] [-t <value>] [-m <value>] [-i <value> | --input-file
    <value>] [-s] [-o]

ARGUMENTS
  ACTORID  Name or ID of the Actor to run (e.g. "my-actor", "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not
           provided, the command runs the remote Actor specified in the ".actor/actor.json" file.

FLAGS
  -b, --build=<value>       Tag or number of the build to run (e.g. "latest" or "1.2.34").
  -i, --input=<value>       Optional JSON input to be given to the Actor.
  -m, --memory=<value>      Amount of memory allocated for the Actor run, in megabytes.
  -o, --output-dataset      Prints out the entire default dataset on successful run of the Actor.
  -s, --silent              Prevents printing the logs of the Actor run to the console.
  -t, --timeout=<value>     Timeout for the Actor run in seconds. Zero value means there is no timeout.
      --input-file=<value>  Optional path to a file with JSON input to be given to the Actor. The file must be a valid
                            JSON file. You can also specify `-` to read from standard input.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Runs a specific Actor remotely on the Apify cloud platform.
  The Actor is run under your current Apify account. Therefore you need to be logged in by calling "apify login". It
  takes input for the Actor from the default local key-value store by default.
```

_See code: [src/commands/call.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/call.ts)_

## `apify create [ACTORNAME]`

Creates a new Actor project directory from a selected boilerplate template.

```
USAGE
  $ apify create [ACTORNAME] [-t <value>] [--skip-dependency-install] [--omit-optional-deps]

ARGUMENTS
  ACTORNAME  Name of the Actor and its directory

FLAGS
  -t, --template=<value>         Template for the Actor. If not provided, the command will prompt for it.
                                 Visit
                                 https://raw.githubusercontent.com/apify/actor-templates/master/templates/manifest.json
                                 to find available template names.
      --omit-optional-deps       Skip installing optional dependencies.
      --skip-dependency-install  Skip installing Actor dependencies.

DESCRIPTION
  Creates a new Actor project directory from a selected boilerplate template.
```

_See code: [src/commands/create.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/create.ts)_

## `apify datasets`

Commands are designed to be used with Datasets.

```
USAGE
  $ apify datasets

DESCRIPTION
  Commands are designed to be used with Datasets.
```

_See code: [src/commands/datasets/index.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/datasets/index.ts)_

## `apify datasets create [DATASETNAME]`

Creates a new Dataset on your account

```
USAGE
  $ apify datasets create [DATASETNAME] [--json]

ARGUMENTS
  DATASETNAME  Optional name for the Dataset

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Creates a new Dataset on your account
```

_See code: [src/commands/datasets/create.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/datasets/create.ts)_

## `apify datasets get-items DATASETID`

Exports the items present in a Dataset.

```
USAGE
  $ apify datasets get-items DATASETID [--limit <value>] [--offset <value>] [--format json|jsonl|csv|html|rss|xml|xlsx]

ARGUMENTS
  DATASETID  The ID of the Dataset to export the items for

FLAGS
  --format=<option>  [default: json] The format of the returned output. By default, it is set to 'json'
                     <options: json|jsonl|csv|html|rss|xml|xlsx>
  --limit=<value>    The amount of elements to get from the dataset. By default, it will return all available items.
  --offset=<value>   The offset in the dataset where to start getting items.

DESCRIPTION
  Exports the items present in a Dataset.
```

_See code: [src/commands/datasets/get-items.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/datasets/get-items.ts)_

## `apify datasets ls`

Lists all Datasets on your account.

```
USAGE
  $ apify datasets ls [--json] [--offset <value>] [--limit <value>] [--desc] [--unnamed]

FLAGS
  --desc            Sorts Datasets in descending order.
  --limit=<value>   [default: 20] Number of Datasets that will be listed.
  --offset=<value>  Number of Datasets that will be skipped.
  --unnamed         Lists Datasets that don't have a name set.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Lists all Datasets on your account.
```

_See code: [src/commands/datasets/ls.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/datasets/ls.ts)_

## `apify datasets push-items NAMEORID ITEM`

Pushes an object or an array of objects to the provided Dataset.

```
USAGE
  $ apify datasets push-items NAMEORID ITEM

ARGUMENTS
  NAMEORID  The Dataset ID or name to push the objects to
  ITEM      The object or array of objects to be pushed.

DESCRIPTION
  Pushes an object or an array of objects to the provided Dataset.
```

_See code: [src/commands/datasets/push-items.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/datasets/push-items.ts)_

## `apify datasets rename NAMEORID [NEWNAME]`

Renames a Dataset, or removes its unique name

```
USAGE
  $ apify datasets rename NAMEORID [NEWNAME] [--unname]

ARGUMENTS
  NAMEORID  The Dataset ID or name to delete
  NEWNAME   The new name for the Dataset

FLAGS
  --unname  Removes the unique name of the Dataset

DESCRIPTION
  Renames a Dataset, or removes its unique name
```

_See code: [src/commands/datasets/rename.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/datasets/rename.ts)_

## `apify datasets rm DATASETNAMEORID`

Deletes a Dataset

```
USAGE
  $ apify datasets rm DATASETNAMEORID

ARGUMENTS
  DATASETNAMEORID  The Dataset ID or name to delete

DESCRIPTION
  Deletes a Dataset
```

_See code: [src/commands/datasets/rm.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/datasets/rm.ts)_

## `apify help [COMMAND]`

Display help for apify.

```
USAGE
  $ apify help [COMMAND...] [-n]

ARGUMENTS
  COMMAND...  Command to show help for.

FLAGS
  -n, --nested-commands  Include all nested commands in the output.

DESCRIPTION
  Display help for apify.
```

_See code: [@oclif/plugin-help](https://github.com/oclif/plugin-help/blob/v6.2.16/src/commands/help.ts)_

## `apify info`

Displays information about the currently active Apify account.

```
USAGE
  $ apify info

DESCRIPTION
  Displays information about the currently active Apify account.
  The information is printed to the console.
```

_See code: [src/commands/info.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/info.ts)_

## `apify init [ACTORNAME]`

Initializes a new Actor project in an existing directory.

```
USAGE
  $ apify init [ACTORNAME] [-y]

ARGUMENTS
  ACTORNAME  Name of the Actor. If not provided, you will be prompted for it.

FLAGS
  -y, --yes  Automatic yes to prompts; assume "yes" as answer to all prompts. Note that in some cases, the command may
             still ask for confirmation.

DESCRIPTION
  Initializes a new Actor project in an existing directory.
  If the directory contains a Scrapy project in Python, the command automatically creates wrappers so that you can run
  your scrapers without changes.

  The command creates the ".actor/actor.json" file and the "storage" directory in the current directory, but does not
  touch any other existing files or directories.

  WARNING: The directory at "storage" will be overwritten if it already exists.
```

_See code: [src/commands/init.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/init.ts)_

## `apify key-value-stores`

Commands are designed to be used with Key Value Stores.

```
USAGE
  $ apify key-value-stores

DESCRIPTION
  Commands are designed to be used with Key Value Stores.

  Aliases: kvs
```

_See code: [src/commands/key-value-stores/index.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/key-value-stores/index.ts)_

## `apify key-value-stores create [KEYVALUESTORENAME]`

Creates a new Key-value store on your account

```
USAGE
  $ apify key-value-stores create [KEYVALUESTORENAME] [--json]

ARGUMENTS
  KEYVALUESTORENAME  Optional name for the Key-value store

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Creates a new Key-value store on your account
```

_See code: [src/commands/key-value-stores/create.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/key-value-stores/create.ts)_

## `apify key-value-stores delete-value STOREID ITEMKEY`

Delete a value from a key-value store.

```
USAGE
  $ apify key-value-stores delete-value STOREID ITEMKEY

ARGUMENTS
  STOREID  The key-value store ID to delete the value from.
  ITEMKEY  The key of the item in the key-value store.

DESCRIPTION
  Delete a value from a key-value store.
```

_See code: [src/commands/key-value-stores/delete-value.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/key-value-stores/delete-value.ts)_

## `apify key-value-stores get-value KEYVALUESTOREID ITEMKEY`

Gets a value by key in the given key-value store.

```
USAGE
  $ apify key-value-stores get-value KEYVALUESTOREID ITEMKEY [--only-content-type]

ARGUMENTS
  KEYVALUESTOREID  The key-value store ID to get the value from.
  ITEMKEY          The key of the item in the key-value store.

FLAGS
  --only-content-type  Only return the content type of the specified key

DESCRIPTION
  Gets a value by key in the given key-value store.
```

_See code: [src/commands/key-value-stores/get-value.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/key-value-stores/get-value.ts)_

## `apify key-value-stores keys STOREID`

Lists all keys in a key-value store.

```
USAGE
  $ apify key-value-stores keys STOREID [--json] [--limit <value>] [--exclusive-start-key <value>]

ARGUMENTS
  STOREID  The key-value store ID to list keys for.

FLAGS
  --exclusive-start-key=<value>  The key to start the list from.
  --limit=<value>                [default: 20] The maximum number of keys to return.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Lists all keys in a key-value store.
```

_See code: [src/commands/key-value-stores/keys.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/key-value-stores/keys.ts)_

## `apify key-value-stores ls`

Lists all Key-value stores on your account.

```
USAGE
  $ apify key-value-stores ls [--json] [--offset <value>] [--limit <value>] [--desc] [--unnamed]

FLAGS
  --desc            Sorts Key-value stores in descending order.
  --limit=<value>   [default: 20] Number of Key-value stores that will be listed.
  --offset=<value>  Number of Key-value stores that will be skipped.
  --unnamed         Lists Key-value stores that don't have a name set.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Lists all Key-value stores on your account.
```

_See code: [src/commands/key-value-stores/ls.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/key-value-stores/ls.ts)_

## `apify key-value-stores rename KEYVALUESTORENAMEORID [NEWNAME]`

Renames a Key-value store, or removes its unique name

```
USAGE
  $ apify key-value-stores rename KEYVALUESTORENAMEORID [NEWNAME] [--unname]

ARGUMENTS
  KEYVALUESTORENAMEORID  The Key-value store ID or name to delete
  NEWNAME                The new name for the Key-value store

FLAGS
  --unname  Removes the unique name of the Key-value store

DESCRIPTION
  Renames a Key-value store, or removes its unique name
```

_See code: [src/commands/key-value-stores/rename.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/key-value-stores/rename.ts)_

## `apify key-value-stores rm KEYVALUESTORENAMEORID`

Deletes a Key-value store

```
USAGE
  $ apify key-value-stores rm KEYVALUESTORENAMEORID

ARGUMENTS
  KEYVALUESTORENAMEORID  The Key-value store ID or name to delete

DESCRIPTION
  Deletes a Key-value store
```

_See code: [src/commands/key-value-stores/rm.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/key-value-stores/rm.ts)_

## `apify key-value-stores set-value STOREID ITEMKEY [VALUE]`

Sets a value in a key-value store.

```
USAGE
  $ apify key-value-stores set-value STOREID ITEMKEY [VALUE] [--content-type <value>]

ARGUMENTS
  STOREID  The key-value store ID to set the value in.
  ITEMKEY  The key of the item in the key-value store.
  VALUE    The value to set.

FLAGS
  --content-type=<value>  [default: application/json] The MIME content type of the value. By default, "application/json"
                          is assumed.

DESCRIPTION
  Sets a value in a key-value store.
```

_See code: [src/commands/key-value-stores/set-value.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/key-value-stores/set-value.ts)_

## `apify login`

Logs in to your Apify account.

```
USAGE
  $ apify login [-t <value>] [-m console|manual]

FLAGS
  -m, --method=<option>  [Optional] Method of logging in to Apify
                         <options: console|manual>
  -t, --token=<value>    [Optional] Apify API token

DESCRIPTION
  Logs in to your Apify account.
  The API token and other account information is stored in the ~/.apify directory, from where it is read by all other
  "apify" commands. To log out, call "apify logout".
```

_See code: [src/commands/login.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/login.ts)_

## `apify logout`

Logs out of your Apify account.

```
USAGE
  $ apify logout

DESCRIPTION
  Logs out of your Apify account.
  The command deletes the API token and all other account information stored in the ~/.apify directory. To log in again,
  call "apify login".
```

_See code: [src/commands/logout.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/logout.ts)_

## `apify pull [ACTORID]`

Pulls an Actor from the Apify platform to the current directory. If it is defined as Git repository, it will be cloned. If it is defined as Web IDE, it will fetch the files.

```
USAGE
  $ apify pull [ACTORID] [-v <value>] [--dir <value>]

ARGUMENTS
  ACTORID  Name or ID of the Actor to run (e.g. "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not provided, the
           command will update the Actor in the current directory based on its name in ".actor/actor.json" file.

FLAGS
  -v, --version=<value>  Actor version number which will be pulled, e.g. 1.2. Default: the highest version
      --dir=<value>      Directory where the Actor should be pulled to

DESCRIPTION
  Pulls an Actor from the Apify platform to the current directory. If it is defined as Git repository, it will be
  cloned. If it is defined as Web IDE, it will fetch the files.
```

_See code: [src/commands/pull.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/pull.ts)_

## `apify push [ACTORID]`

Uploads the Actor to the Apify platform and builds it there.

```
USAGE
  $ apify push [ACTORID] [-v <value>] [-b <value>] [-w <value>] [--no-prompt] [--force] [--dir <value>]

ARGUMENTS
  ACTORID  Name or ID of the Actor to push (e.g. "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not provided, the
           command will create or modify the Actor with the name specified in ".actor/actor.json" file.

FLAGS
  -b, --build-tag=<value>        Build tag to be applied to the successful Actor build. By default, it is taken from the
                                 ".actor/actor.json" file
  -v, --version=<value>          Actor version number to which the files should be pushed. By default, it is taken from
                                 the ".actor/actor.json" file.
  -w, --wait-for-finish=<value>  Seconds for waiting to build to finish, if no value passed, it waits forever.
      --dir=<value>              Directory where the Actor is located
      --force                    Push an Actor even when the local files are older than the Actor on the platform.
      --no-prompt                Do not prompt for opening the Actor details in a browser. This will also not open the
                                 browser automatically.

DESCRIPTION
  Uploads the Actor to the Apify platform and builds it there.
  The Actor settings are read from the ".actor/actor.json" file in the current directory, but they can be overridden
  using command-line options.
  NOTE: If the source files are smaller than 3 MB then they are uploaded as
  "Multiple source files", otherwise they are uploaded as "Zip file".

  When there's an attempt to push files that are older than the Actor on the platform, the command will fail. Can be
  overwritten with --force flag.
```

_See code: [src/commands/push.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/push.ts)_

## `apify request-queues`

Commands are designed to be used with Request Queues.

```
USAGE
  $ apify request-queues

DESCRIPTION
  Commands are designed to be used with Request Queues.
```

_See code: [src/commands/request-queues/index.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/request-queues/index.ts)_

## `apify run`

Runs the Actor locally in the current directory.

```
USAGE
  $ apify run [-p] [--purge-queue] [--purge-dataset] [--purge-key-value-store] [--entrypoint <value>] [-i
    <value> | --input-file <value>]

FLAGS
  -i, --input=<value>          Optional JSON input to be given to the Actor.
  -p, --purge                  Shortcut that combines the --purge-queue, --purge-dataset and --purge-key-value-store
                               options.
      --entrypoint=<value>     Optional entrypoint for running with injected environment variables.
                               For Python, it is the module name, or a path to a file.
                               For node.js, it is the npm script name, or a path to a JS/MJS file. You can also pass in
                               a directory name, provided that directory contains an "index.js" file.
      --input-file=<value>     Optional path to a file with JSON input to be given to the Actor. The file must be a
                               valid JSON file. You can also specify `-` to read from standard input.
      --purge-dataset          Deletes the local directory containing the default dataset before the run starts.
      --purge-key-value-store  Deletes all records from the default key-value store in the local directory before the
                               run starts, except for the "INPUT" key.
      --purge-queue            Deletes the local directory containing the default request queue before the run starts.

DESCRIPTION
  Runs the Actor locally in the current directory.
  It sets various APIFY_XYZ environment variables in order to provide a working execution environment for the Actor. For
  example, this causes the Actor input, as well as all other data in key-value stores, datasets or request queues to be
  stored in the "storage" directory, rather than on the Apify platform.

  NOTE: You can override the command's default behavior for Node.js Actors by overriding the "start" script in the
  package.json file. You can set up your own main file or environment variables by changing it.
```

_See code: [src/commands/run.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/run.ts)_

## `apify runs`

Commands are designed to be used with Actor Runs.

```
USAGE
  $ apify runs

DESCRIPTION
  Commands are designed to be used with Actor Runs.
```

_See code: [src/commands/runs/index.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/runs/index.ts)_

## `apify runs abort RUNID`

Aborts an Actor Run.

```
USAGE
  $ apify runs abort RUNID [--json] [-f]

ARGUMENTS
  RUNID  The run ID to abort.

FLAGS
  -f, --force  Whether to force the run to abort immediately, instead of gracefully.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Aborts an Actor Run.
```

_See code: [src/commands/runs/abort.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/runs/abort.ts)_

## `apify runs info RUNID`

Prints information about an Actor Run.

```
USAGE
  $ apify runs info RUNID [--json] [-v]

ARGUMENTS
  RUNID  The run ID to print information about.

FLAGS
  -v, --verbose  Prints more in-depth information about the Actor Run.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Prints information about an Actor Run.
```

_See code: [src/commands/runs/info.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/runs/info.ts)_

## `apify runs log RUNID`

Prints the log of a specific run.

```
USAGE
  $ apify runs log RUNID

ARGUMENTS
  RUNID  The run ID to get the log from.

DESCRIPTION
  Prints the log of a specific run.
```

_See code: [src/commands/runs/log.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/runs/log.ts)_

## `apify runs ls [ACTORID]`

Lists all runs of the Actor.

```
USAGE
  $ apify runs ls [ACTORID] [--json] [--offset <value>] [--limit <value>] [--desc] [-c]

ARGUMENTS
  ACTORID  Optional Actor ID or Name to list runs for. By default, it will use the Actor from the current directory.

FLAGS
  -c, --compact         Display a compact table.
      --desc            Sort runs in descending order.
      --limit=<value>   [default: 10] Number of runs that will be listed.
      --offset=<value>  Number of runs that will be skipped.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Lists all runs of the Actor.
```

_See code: [src/commands/runs/ls.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/runs/ls.ts)_

## `apify runs resurrect RUNID`

Resurrects an aborted or finished Actor Run.

```
USAGE
  $ apify runs resurrect RUNID [--json]

ARGUMENTS
  RUNID  The run ID to resurrect.

GLOBAL FLAGS
  --json  Format output as json.

DESCRIPTION
  Resurrects an aborted or finished Actor Run.
```

_See code: [src/commands/runs/resurrect.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/runs/resurrect.ts)_

## `apify runs rm RUNID`

Deletes an Actor Run.

```
USAGE
  $ apify runs rm RUNID

ARGUMENTS
  RUNID  The run ID to delete.

DESCRIPTION
  Deletes an Actor Run.
```

_See code: [src/commands/runs/rm.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/runs/rm.ts)_

## `apify secrets`

Manages secret values for Actor environment variables.

```
USAGE
  $ apify secrets

DESCRIPTION
  Manages secret values for Actor environment variables.

  Example:
  $ apify secrets add mySecret TopSecretValue123

  Now the "mySecret" value can be used in an environment variable defined in ".actor/actor.json" file by adding the "@"
  prefix:

  {
  "actorSpecification": 1,
  "name": "my_actor",
  "environmentVariables": { "SECRET_ENV_VAR": "@mySecret" },
  "version": "0.1
  }

  When the Actor is pushed to Apify cloud, the "SECRET_ENV_VAR" and its value is stored as a secret environment variable
  of the Actor.
```

_See code: [src/commands/secrets/index.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/secrets/index.ts)_

## `apify secrets add NAME VALUE`

Adds a new secret value.

```
USAGE
  $ apify secrets add NAME VALUE

ARGUMENTS
  NAME   Name of the secret
  VALUE  Value of the secret

DESCRIPTION
  Adds a new secret value.
  The secrets are stored to a file at ~/.apify
```

_See code: [src/commands/secrets/add.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/secrets/add.ts)_

## `apify secrets rm NAME`

Removes the secret.

```
USAGE
  $ apify secrets rm NAME

ARGUMENTS
  NAME  Name of the secret

DESCRIPTION
  Removes the secret.
```

_See code: [src/commands/secrets/rm.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/secrets/rm.ts)_

## `apify task`

Commands are designed to be used to interact with Tasks.

```
USAGE
  $ apify task

DESCRIPTION
  Commands are designed to be used to interact with Tasks.
```

_See code: [src/commands/task/index.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/task/index.ts)_

## `apify task run TASKID`

Runs a specific Actor remotely on the Apify cloud platform.

```
USAGE
  $ apify task run TASKID [-b <value>] [-t <value>] [-m <value>]

ARGUMENTS
  TASKID  Name or ID of the Task to run (e.g. "my-task" or "E2jjCZBezvAZnX8Rb").

FLAGS
  -b, --build=<value>    Tag or number of the build to run (e.g. "latest" or "1.2.34").
  -m, --memory=<value>   Amount of memory allocated for the Task run, in megabytes.
  -t, --timeout=<value>  Timeout for the Task run in seconds. Zero value means there is no timeout.

DESCRIPTION
  Runs a specific Actor remotely on the Apify cloud platform.
  The Actor is run under your current Apify account. Therefore you need to be logged in by calling "apify login". It
  takes input for the Actor from the default local key-value store by default.
```

_See code: [src/commands/task/run.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/task/run.ts)_

## `apify validate-schema [PATH]`

Validates input schema and prints errors found.

```
USAGE
  $ apify validate-schema [PATH]

ARGUMENTS
  PATH  Optional path to your INPUT_SCHEMA.json file. If not provided ./INPUT_SCHEMA.json is used.

DESCRIPTION
  Validates input schema and prints errors found.
  The input schema for the Actor is used from these locations in order of preference.
  The first one found is validated as it would be the one used on the Apify platform.
  1. Directly embedded object in ".actor/actor.json" under 'input' key
  2. Path to JSON file referenced in ".actor/actor.json" under 'input' key
  3. JSON file at .actor/INPUT_SCHEMA.json
  4. JSON file at INPUT_SCHEMA.json

  You can also pass any custom path to your input schema to have it validated instead.
```

_See code: [src/commands/validate-schema.ts](https://github.com/apify/apify-cli/blob/v0.21.0/src/commands/validate-schema.ts)_
<!-- commandsstop -->
<!-- prettier-ignore-end -->


================================================
File: /docs/telemetry.md
================================================
---
sidebar_label: Telemetry
title: Telemetry
---

Apify collects telemetry data about the general usage of the CLI to help us improve the product. Participation in this program is optional and you may opt out if you prefer not to share any information.

## Data Collection

All telemetry data is collected and stored securely on [Mixpanel](https://mixpanel.com/). We do not collect any sensitive information such as your API token or personal information.

### Metrics Collected

Before a user connects to the Apify platform, we collect anonymous information about CLI usage including:

- Usage of all commands
- Internal attributes of the local environment (OS, shell, Node.js version, Python version, Apify CLI version)
- For the `actor create` command, we identify which template was used to create the Actor (language, template name, template ID)

After a user connects to the Apify platform (successful `apify login`), we collect the same information about CLI usage along with the ID of the connected user. You can read more about how we protect personal information in our [Privacy Policy](https://apify.com/privacy-policy).

## How to opt out

You can disable telemetry by setting the "APIFY_CLI_DISABLE_TELEMETRY" environment variable to "1". After setting this variable, the CLI will not send any telemetry data whether you are connected with Apify or not.


================================================
File: /docs/index.md
================================================
---
title: Apify CLI
---

<a href="https://www.npmjs.com/package/apify-cli"><img src="https://badge.fury.io/js/apify-cli.svg" alt="npm version" loading="lazy" /></a>
<a href="https://travis-ci.com/apify/apify-cli?branch=master"><img src="https://travis-ci.com/apify/apify-cli.svg?branch=master" loading="lazy" alt="Build Status" /></a>

Apify command-line interface (Apify CLI) helps you create, develop, build and run
[Apify Actors](https://apify.com/actors),
and manage the Apify cloud platform from any computer.

Apify Actors are cloud programs that can perform arbitrary web scraping, automation or data processing job.
They accept input, perform their job and generate output.
While you can develop Actors in an online IDE directly in the [Apify web application](https://console.apify.com/),
for complex projects it is more convenient to develop Actors locally on your computer
using <a href="https://github.com/apify/apify-sdk-js">Apify SDK</a>
and only push the Actors to the Apify cloud during deployment.
This is where the Apify CLI comes in.

Note that Actors running on the Apify platform are executed in Docker containers, so with an appropriate `Dockerfile`
you can build your Actors in any programming language.
However, we recommend using JavaScript / Node.js, for which we provide most libraries and support.


================================================
File: /docs/installation.md
================================================
---
title: Installation
description: Learn how to install Apify CLI, and how to create, run, and manage Actors through it.
sidebar_label: Installation
---

## Installation

You can install Apify CLI either using [Homebrew package manager](https://brew.sh) on macOS or Linux or using NPM on all platforms including Windows.

### Via Homebrew

Run the following command:

```bash showLineNumbers
brew install apify-cli
```

### Via NPM

First, make sure you have [Node.js](https://nodejs.org) version 18 or higher with NPM installed on your computer:

```bash showLineNumbers
node --version
npm --version
```

Install or upgrade Apify CLI by running:

```bash showLineNumbers
npm -g install apify-cli
```

If you receive a permission error, read npm's [official guide](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally) on installing packages globally.

Alternatively, you can use [Node Version Manager (nvm)](https://github.com/nvm-sh/nvm) and install Apify CLI only into a selected user-level Node version without requiring root privileges:

```bash showLineNumbers
nvm install 18
nvm use 18
npm -g install apify-cli
```

After using either of these methods , verify that Apify CLI was installed correctly by running:

```bash showLineNumbers
apify --version
```

which should print something like:

```bash showLineNumbers
apify-cli/0.19.1 linux-x64 node-v18.17.0
```

## Basic Usage

The following examples demonstrate the basic usage of Apify CLI.

### Create a New Actor from Scratch

```bash showLineNumbers
apify create my-hello-world
```

First, you will be prompted to select a template with the boilerplate for the Actor, to help you get started quickly.
The command will create a directory called `my-hello-world` that contains a Node.js project
for the Actor and a few configuration files.

### Create a New Actor from Existing Project

:::tip Automatic Actor directory initialization
When you create an Actor using the `apify create` command, the directory will already be initialized.
:::

```bash showLineNumbers
cd ./my/awesome/project
apify init
```

This command will only set up local Actor development environment in an existing directory,
i.e. it will create the `.actor/actor.json` file and `apify_storage` directory.

Before you can run your project locally using `apify run`, you have to set up the right start command in `package.json` under scripts.start. For example:

```json showLineNumbers
{
    ...
    "scripts": {
        "start": "node your_main_file.js",
    },
    ...
}
```

You can find more information about by running `apify help run`.

### Run the Actor Locally

```bash showLineNumbers
cd my-hello-world
apify run
```

This command runs the Actor on your local machine.
Now's your chance to develop the logic - or magic :smirk:

### Login with your Apify account

```bash showLineNumbers
apify login
```

Before you can interact with the Apify cloud, you need to [create an Apify account](https://console.apify.com/)
and log in to it using the above command. You will be prompted for
your [Apify API token](https://console.apify.com/settings/integrations).

:::note API token save directory
The command will store the API token and other sensitive information to `~/.apify`.
:::

### Push the Actor to the Apify Cloud

```bash showLineNumbers
apify push
```

This command uploads your project to the Apify cloud and builds an Actor from it. On the platform, Actor needs to be built before it can be run.

### Run an Actor on the Apify Cloud

```bash showLineNumbers
apify call
```

Runs the Actor corresponding to the current directory on the Apify Platform.

This command can also be used to run other Actors, for example:

```bash showLineNumbers
apify call apify/hello-world
```

### So what's in this `.actor/actor.json` File?

This file associates your local development project with an Actor on the Apify Platform.
It contains information such as Actor name, version, build tag and environment variables.
Make sure you commit this file to the Git repository.

For example, `.actor/actor.json` file can look as follows:

```json showLineNumbers
{
  "actorSpecification": 1,
  "name": "name-of-my-scraper",
  "version": "0.0",
  "buildTag": "latest",
  "environmentVariables": {
    "MYSQL_USER": "my_username",
    "MYSQL_PASSWORD": "@mySecretPassword"
  },
  "dockerfile": "./Dockerfile",
  "readme": "./ACTOR.md",
  "input": "./input_schema.json",
  "storages": {
    "dataset": "./dataset_schema.json"
  }
}
```

**`Dockerfile` field**

If you specify the path to your Docker file under the `dockerfile` field, this file will be used for Actor builds on the platform. If not specified, the system will look for Docker files at `.actor/Dockerfile` and `Dockerfile` in this order of preference.

**`Readme` field**

If you specify the path to your readme file under the `readme` field, the readme at this path will be used on the platform. If not specified, readme at `.actor/README.md` and `README.md` will be used in this order of preference.

**`Input` field**

You can embed your [input schema](https://docs.apify.com/actors/development/input-schema#specification-version-1) object directly in `actor.json` under `input` field. Alternatively, you can provide a path to a custom input schema. If not provided, the input schema at `.actor/INPUT_SCHEMA.json` and `INPUT_SCHEMA.json` is used in this order of preference.

**`Storages.dataset` field**

You can define the schema of the items in your dataset under the `storages.dataset` field. This can be either an embedded object or a path to a JSON schema file. You can read more about the schema of your Actor output [here](https://docs.apify.com/actors/development/output-schema#specification-version-1).

:::note Migration from deprecated config "apify.json"
Note that previously, Actor config was stored in the `apify.json` file that has been deprecated. You can find the (very slight) differences and migration info in [migration guidelines](https://github.com/apify/apify-cli/blob/master/MIGRATIONS.md).
:::


================================================
File: /tsconfig.typechecking.json
================================================
{
	"extends": "./tsconfig.json",
	"compilerOptions": {
		"rootDir": ".",
		"noEmit": true,
		"allowImportingTsExtensions": true,
		"useUnknownInCatchVariables": false,
		"tsBuildInfoFile": "dist/typechecking.tsbuildinfo",
		"checkJs": true
	},
	"include": ["src", "bin"]
}


================================================
File: /cucumber.json
================================================
{
	"default": {
		"import": ["features/**/*.ts"],
		"parallel": 4
	}
}


================================================
File: /CHANGELOG.md
================================================
# Changelog

All notable changes to this project will be documented in this file.

<!-- git-cliff-unreleased-start -->

## 0.20.8 - **not yet released**

### 🚀 Features

- Builds namespace ([#620](https://github.com/apify/apify-cli/pull/620)) ([6345162](https://github.com/apify/apify-cli/commit/6345162e44a00b404b4f95c2c80c2e437eff1d62)) by [@vladfrangu](https://github.com/vladfrangu)
- `runs ls` ([#640](https://github.com/apify/apify-cli/pull/640)) ([dd84d37](https://github.com/apify/apify-cli/commit/dd84d37c6ea89c64db712c7c94709f3181a7bd1f)) by [@vladfrangu](https://github.com/vladfrangu)
- `runs abort` ([#643](https://github.com/apify/apify-cli/pull/643)) ([96e5a34](https://github.com/apify/apify-cli/commit/96e5a3435cca08d87dc8d39659a7a6524f18be0e)) by [@vladfrangu](https://github.com/vladfrangu)
- `runs resurrect` ([#644](https://github.com/apify/apify-cli/pull/644)) ([7dbf4fb](https://github.com/apify/apify-cli/commit/7dbf4fb06c657246563c1c64e76ad83f283ea275)) by [@vladfrangu](https://github.com/vladfrangu)
- `runs log` ([#645](https://github.com/apify/apify-cli/pull/645)) ([dd6af5e](https://github.com/apify/apify-cli/commit/dd6af5ece79f4399fc5065483b650c71c61114cf)) by [@vladfrangu](https://github.com/vladfrangu)
- `runs rm` &amp; `builds rm` &amp; `actors rm` ([#648](https://github.com/apify/apify-cli/pull/648)) ([566f8c5](https://github.com/apify/apify-cli/commit/566f8c5d1482f150f4d61229524c7672c2af666d)) by [@vladfrangu](https://github.com/vladfrangu)
- `runs info` ([#657](https://github.com/apify/apify-cli/pull/657)) ([827767c](https://github.com/apify/apify-cli/commit/827767cfc988b7d587adceb825765e553deeed77)) by [@vladfrangu](https://github.com/vladfrangu)
- `actors build` ([#661](https://github.com/apify/apify-cli/pull/661)) ([4605cda](https://github.com/apify/apify-cli/commit/4605cda7f3a4f5a35160ba69bf4a454c889dd813)) by [@vladfrangu](https://github.com/vladfrangu)
- `actors pull` ([#662](https://github.com/apify/apify-cli/pull/662)) ([26d5cb3](https://github.com/apify/apify-cli/commit/26d5cb356fbb38a789e9b88f4d4b01468e38bd26)) by [@vladfrangu](https://github.com/vladfrangu)
- `actors call` ([#663](https://github.com/apify/apify-cli/pull/663)) ([a472300](https://github.com/apify/apify-cli/commit/a4723007e65bde8db6eb121a0dc38e2c7bc6caec)) by [@vladfrangu](https://github.com/vladfrangu)
- Check if cli was installed using volta when checking for updates ([#667](https://github.com/apify/apify-cli/pull/667)) ([aee0233](https://github.com/apify/apify-cli/commit/aee023336768e59fd4ff8d6c957f804d315e7bf3)) by [@vladfrangu](https://github.com/vladfrangu)
- `actors start` ([#669](https://github.com/apify/apify-cli/pull/669)) ([45956e2](https://github.com/apify/apify-cli/commit/45956e224305dd040b607d1fc3ff5cbbc8b28f32)) by [@vladfrangu](https://github.com/vladfrangu)
- `actors push` ([#671](https://github.com/apify/apify-cli/pull/671)) ([d77c531](https://github.com/apify/apify-cli/commit/d77c5314d4252a6bbf30718436dd84467aa35d7f)) by [@vladfrangu](https://github.com/vladfrangu)
- `actors ls` ([#675](https://github.com/apify/apify-cli/pull/675)) ([de258cb](https://github.com/apify/apify-cli/commit/de258cb8872857aa559afb4b16ed5a52f4fb2094)) by [@vladfrangu](https://github.com/vladfrangu)
- `key-value-stores get-value` ([#678](https://github.com/apify/apify-cli/pull/678)) ([67cfefe](https://github.com/apify/apify-cli/commit/67cfefef88fac220a1c959aaaecf3d051e482236)) by [@vladfrangu](https://github.com/vladfrangu)
- `datasets get-items` ([#679](https://github.com/apify/apify-cli/pull/679)) ([b521546](https://github.com/apify/apify-cli/commit/b521546df195bab7bedf5534167b6edae6a5e69e)) by [@vladfrangu](https://github.com/vladfrangu)
- `datasets` &#x2F; `key-value-stores` commands ([#685](https://github.com/apify/apify-cli/pull/685)) ([c7d77e1](https://github.com/apify/apify-cli/commit/c7d77e1cec711edd9996cbb1249e489fbf3db547)) by [@vladfrangu](https://github.com/vladfrangu)
- Key-value-store commands ([#700](https://github.com/apify/apify-cli/pull/700)) ([eb8ff3b](https://github.com/apify/apify-cli/commit/eb8ff3b9c7f1319d0937543f7b0b97cb25d6390a)) by [@vladfrangu](https://github.com/vladfrangu)
- `actors info` ([#701](https://github.com/apify/apify-cli/pull/701)) ([0f4b3f0](https://github.com/apify/apify-cli/commit/0f4b3f08dd5937ca6664342c2510a9f4f3fa52f6)) by [@vladfrangu](https://github.com/vladfrangu)

### 🐛 Bug Fixes

- Look for lowercase input schema in default paths ([#647](https://github.com/apify/apify-cli/pull/647)) ([68456e6](https://github.com/apify/apify-cli/commit/68456e63eee3c28e7c0ee7464a2cbc1a00ba9dfa)) by [@mvolfik](https://github.com/mvolfik)
- Emit warning if input.json is modified during run and prefilled with defaults ([#672](https://github.com/apify/apify-cli/pull/672)) ([8a6fd3f](https://github.com/apify/apify-cli/commit/8a6fd3f60523380041309db830a62f52cc60e4d4)) by [@vladfrangu](https://github.com/vladfrangu), closes [#670](https://github.com/apify/apify-cli/issues/670)
- Scrapy wrapping being broken due to ESM migration ([#686](https://github.com/apify/apify-cli/pull/686)) ([e2a7591](https://github.com/apify/apify-cli/commit/e2a7591070a284394643e8dbb03bc020939ff61f)) by [@vladfrangu](https://github.com/vladfrangu)
- **ci:** Make it work + publish with provenances ([#694](https://github.com/apify/apify-cli/pull/694)) ([e41ea72](https://github.com/apify/apify-cli/commit/e41ea728a9177dcec4ea73c25128cddebc00dd79)) by [@vladfrangu](https://github.com/vladfrangu)
- Handle stdin correctly from slower stdout emitting ([#704](https://github.com/apify/apify-cli/pull/704)) ([a5b53de](https://github.com/apify/apify-cli/commit/a5b53de480aad3caf80e1a9439cd5e64648fe312)) by [@vladfrangu](https://github.com/vladfrangu)
- Running commands with spaces on windows ([#715](https://github.com/apify/apify-cli/pull/715)) ([d1c207a](https://github.com/apify/apify-cli/commit/d1c207a703a6948e7b3a6cfe82c5cfa6a3b9222d)) by [@vladfrangu](https://github.com/vladfrangu), closes [#692](https://github.com/apify/apify-cli/issues/692)

<!-- git-cliff-unreleased-end -->

# 0.6.1 / 2020-05-18

- **BREAKING:** Templates are now fully decoupled from this project and
  the [templates repository](https://github.com/apify/actor-templates)
  serves as the single source of truth. Some templates were replaced
  and others were renamed to better clarify their purpose.
- **BREAKING:** Providing an invalid template in `apify.json` no longer
  throws, but rather silently uses a reasonable default configuration.
  This is to support regular changes to templates without breaking older
  versions of the CLI.

  # 0.5.3 / 2020-03-03

- Moved templates to separate repository
- Fixed: creating `apify_storage` in root folder after `apify create` command

  # 0.5.2 / 2020-01-22

- Added bot(dependabot.com) to check latest Apify SDK version in all templates
- Updated apify package in all templates
- Updated npm packages and fixed all npm audit issues

  # 0.5.1 / 2019-12-19

- Added warning about outdated node.js version
- Fixed infinite push, when the previous one was interrupted
- Fixed calling public actors with `apify call`
- `apify init` create empty INPUT.json file

  # 0.5.0 / 2019-11-27

- Drop support for node 8 and 9
- Fix: Pass the --max-http-header-size=80000 to the nodeJs process

  # 0.4.1 / 2019-10-02

- New actor template for Apify projects, you can create it with `apify create --template apify_project`
- `apify vis` - Using improved schema validator

  # 0.4.0 / 2019-09-23

- Breaking Change - `apify push`: Pushes source code as a "Multiple source files" in case source code is less that 3 MB

  # 0.3.12 / 2019-09-18

  Bug fixes:

- `apify create`: Added validation for actor name
- `apify init` skips creation of apify.json if already exists
- `apify run -p` runs actor, if apify_storage doesn't exist
- Updated packages
- Additional minor fixes

  # 0.3.11 / 2019-07-26

- Updated packages
- Updated Cheerio Crawler template
- Updated Apify package version in all templates

  # 0.3.10 / 2019-06-03

- Updated packages

  # 0.3.9 / 2019-05-15

- Improved the templates and texts

  # 0.3.8 / 2019-03-29

- Updated all templates regarding the last version of apify SDK.

  # 0.3.7 / 2019-03-18

- Fixed templates to use Apify.getInput(), replaced deprecated function and options,
  added debug fields, added .idea to .gitignore
- Updated packages
- Fixed bug: Users without username can use push/call command

  # 0.3.6 / 2019-01-29

- Added command `apify vis` that validates actor input schema.

  # 0.3.5 / 2019-01-25

- Upgraded to apify@0.11 in templates

  # 0.3.3 / 2018-12-12

- Omitted CMD command in all templates Dockerfile.

  # 0.3.2 / 2018-12-05

- Updated apify-client package. It fixed bug, when user can not push actor, whe he changed version in apify.json.

  # 0.3.1 / 2018-11-29

- :tada: New commands to manage secret environment variables: `apify secrets:add`, `apify secrets:rm`.
- New documentation how to set environment variable in `apify.json`, see [documentation](https://github.com/apify/apify-cli/blob/master/README.md#environment-variables).
- **BREAKING CHANGES**: Simplified `apify.json` structure. It will be updated automatically before execution apify run and push command.
- Command `apify create` now shows progress bar of npm install.
- Small bugs fixes

  # 0.2.7 / 2018-11-27

- Updated all templates to latest apify packages

  # 0.2.6 / 2018-11-09

- Added warning if `apify run` reuse old state in storage
- Fixed issues #70 #65 #68

  # 0.2.5 / 2018-10-31

- Updated NPM dependencies
- Upgraded to apify-shared@0.1.6
- Fixed templates to use apify/actor-node-chrome Docker image instead of outdated apify/actor-node-puppeteer

  # 0.2.3 / 2018-09-17

- Updated all templates to apify version 0.8.\*
- Added template named hello_word

  # 0.2.1 / 2018-09-17

- **BREAKING CHANGES**: The local storage directories have been renamed and package.json files needs a new `start` command.
  See [migration guide](/MIGRATIONS.md) for existing projects if you are upgrading from 0.1._ to 0.2._.
- You can specified another file that main.js for `apify run` command using npm start script.

  # 0.2.0 / 2018-09-12

- **BREAKING CHANGES**: Version 0.2.0 of Apify CLI supports only version 0.7.0 of API SDK or newer as management of environment variables
  has been changed according to Apify SDK version 0.7.0.
- Dropped support for Node 7

  # 0.1.18 / 2018-09-12

- Updated NPM dependencies, npm-shrinkwrap.json replaced with package-lock.json
- Updated NPM dependencies in code templates

  # 0.1.15 / 2018-07-23

- Rename act to actor

  # 0.1.13 / 2018-07-12

- Add environment variables for enable live view for local actors.

  # 0.1.12 / 2018-06-28

- From now `apify call` and `apify push` commands stream live logs from run and build to your terminal
- Add options -p, --purge, --purge-dataset, --purge-key-value-store, --purge-queue in `apify run` to clean stores before runs actor locally
- Add option -w, --wait-for-finish=wait-for-finish in `apify push` and `apify call` - command waits x seconds to finish run or build on Apify
- Fixes #26, #33, #34, #36, #38, #39, #37, #35

  # 0.1.11 / 2018-05-30

- Use npm-shrinkwrap.json instead of package-lock.json for published module
- Update template, where we using proxy
- Fix #30

  # 0.1.9 / 2018-04-18

- apify run takes APIFY_USER_ID and APIFY_TOKEN as environments variables, if client is logged locally
- apify call takes input from default local key-value-store
- Fix: duplicates new lines in log

  # 0.1.8 / 2018-04-17

- Print warning if you have old version of cli
- apify run - kills all sub processes for SIGINT signal (ctrl+c) - It kills all related browsers in apify run command, related issue:
  https://github.com/apify/apify-js/issues/72

  # 0.1.7 / 2018-04-12

- Readme and templates updates

  # 0.1.6 / 2018-04-11

- Add support for request queue

  # 0.1.5 / 2018-04-09

- Works for windows
- New command apify info

  # 0.1.x / 2018-04-01

- The first public release

  # 0.0.x / 2018-03-01

- Initial development, lot of new stuff


================================================
File: /.github/scripts/before-beta-release.ts
================================================
import { execSync } from 'node:child_process';
import { readFile, writeFile } from 'node:fs/promises';

const PKG_JSON_PATH = new URL('../../package.json', import.meta.url);

const pkgJson = JSON.parse(await readFile(PKG_JSON_PATH, 'utf8'));

const PACKAGE_NAME = pkgJson.name;
const VERSION = pkgJson.version;

const nextVersion = getNextVersion(VERSION);
console.log(`before-deploy: Setting version to ${nextVersion}`);
pkgJson.version = nextVersion;

await writeFile(PKG_JSON_PATH, JSON.stringify(pkgJson, null, 4) + '\n');

function getNextVersion(version: string) {
	const versionString = execSync(`npm show ${PACKAGE_NAME} versions --json`, { encoding: 'utf8' });
	const versions = JSON.parse(versionString) as string[];

	if (versions.some((v) => v === VERSION)) {
		console.error(
			`before-deploy: A release with version ${VERSION} already exists. Please increment version accordingly.`,
		);
		process.exit(1);
	}

	const prereleaseNumbers = versions
		.filter((v) => v.startsWith(VERSION) && v.includes('-'))
		.map((v) => Number(v.match(/\.(\d+)$/)![1]));
	const lastPrereleaseNumber = Math.max(-1, ...prereleaseNumbers);
	return `${version}-beta.${lastPrereleaseNumber + 1}`;
}


================================================
File: /.github/workflows/check.yaml
================================================
# This workflow runs for every pull request to lint and test the proposed changes.

name: Check

on:
    # Push to master will deploy a beta version
    push:
        branches: [master, renovate/**]
    pull_request:
        branches: [master]
    # A release via GitHub releases will deploy a latest version
    release:
        types: [published]

jobs:
    build_and_test:
        name: Build & Test
        if: ${{ !contains(github.event.head_commit.message, '[skip ci]') }}
        runs-on: ${{ matrix.os }}

        strategy:
            fail-fast: false
            matrix:
                os: [ubuntu-latest, windows-latest]
                node-version: [18, 20, 22]

        steps:
            - uses: actions/checkout@v4

            - name: Use Node.js ${{ matrix.node-version }}
              uses: actions/setup-node@v4
              with:
                  node-version: ${{ matrix.node-version }}

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate

            - name: Activate cache for Node.js ${{ matrix.node-version }}
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            - name: Install Dependencies
              run: yarn

            - name: Run Tests
              env:
                  TEST_USER_TOKEN: ${{ secrets.APIFY_TEST_USER_API_TOKEN }}
                  APIFY_CLI_DISABLE_TELEMETRY: 1
              run: yarn test

    test_python_support:
        name: Test Python template support
        strategy:
            fail-fast: false
            matrix:
                os: [ubuntu-latest, windows-latest]
                python-version: ["3.9", "3.10", "3.11", "3.12"]
        runs-on: ${{ matrix.os }}

        steps:
            - uses: actions/checkout@v4

            - name: Use Node.js 20
              uses: actions/setup-node@v4
              with:
                  node-version: 20

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate

            - name: Activate cache for Node.js 20
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            - name: Install Dependencies
              run: yarn

            - name: Set up Python ${{ matrix.python-version }}
              uses: actions/setup-python@v5
              with:
                  python-version: ${{ matrix.python-version }}

            - name: Run Python tests
              env:
                  TEST_USER_TOKEN: ${{ secrets.APIFY_TEST_USER_API_TOKEN }}
                  APIFY_CLI_DISABLE_TELEMETRY: 1
              run: yarn test-python

    docs:
        name: Docs build
        if: ${{ !contains(github.event.head_commit.message, '[skip ci]') }}
        runs-on: ubuntu-latest
        steps:
            - name: Checkout Source code
              uses: actions/checkout@v4

            - name: Use Node.js 20
              uses: actions/setup-node@v4
              with:
                  node-version: 20

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate

            - name: Activate cache for Node.js 20
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            - name: Install Dependencies
              run: yarn

            - name: Build & deploy docs
              run: |
                  cd website
                  yarn
                  yarn build

    lint:
        name: Lint
        runs-on: ubuntu-latest

        steps:
            - uses: actions/checkout@v4

            - name: Use Node.js 20
              uses: actions/setup-node@v4
              with:
                  node-version: 20

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate

            - name: Activate cache for Node.js 20
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            - name: Install Dependencies
              run: yarn

            - name: Run lint checks
              run: yarn lint

            - name: Run format checks
              run: yarn format


================================================
File: /.github/workflows/docs.yaml
================================================
name: docs

on:
    push:
        branches:
            - master
    workflow_dispatch:

jobs:
    build:
        if: ${{ !contains(github.event.head_commit.message, '[skip ci]') }}
        environment:
            name: github-pages
        permissions:
            contents: write
            pages: write
            id-token: write
        runs-on: ubuntu-latest

        steps:
            - uses: actions/checkout@v4
              with:
                  token: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}

            - name: Use Node.js 20
              uses: actions/setup-node@v4
              with:
                  node-version: 20

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate

            - name: Activate cache for Node.js 20
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            - name: Build docs
              run: |
                  # install project deps
                  yarn
                  # update next docs reference
                  yarn update-docs
                  # go to website dir
                  cd website
                  # install website deps
                  yarn
                  # install the latest theme version
                  yarn add @apify/docs-theme@latest
                  # build the docs
                  yarn build
              env:
                  SMARTLOOK_PROJECT_KEY: ${{ secrets.SMARTLOOK_DOCS_PROJECT_KEY }}
                  GIT_USER: "apify-service-account:${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}"
                  GH_TOKEN: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}
                  APIFY_SIGNING_TOKEN: ${{ secrets.APIFY_SIGNING_TOKEN }}

            - name: Commit the updated package(-lock).json
              uses: stefanzweifel/git-auto-commit-action@v5
              with:
                  commit_message: "chore: Automatic theme updating workflow [skip ci]"
                  file_pattern: "website/package*.json website/yarn.lock"
                  commit_user_name: Apify Bot
                  commit_user_email: my-github-actions-bot@example.org
                  commit_author: Apify Bot <apify@apify.com>

            - name: Set up GitHub Pages
              uses: actions/configure-pages@v5

            - name: Upload GitHub Pages artifact
              uses: actions/upload-pages-artifact@v3
              with:
                  path: ./website/build

            - name: Deploy artifact to GitHub Pages
              uses: actions/deploy-pages@v4

            - name: Invalidate CloudFront cache
              run: gh workflow run invalidate.yaml --repo apify/apify-docs-private
              env:
                  GITHUB_TOKEN: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}


================================================
File: /.github/workflows/cucumber.yaml
================================================
name: Cucumber E2E tests

on:
    workflow_dispatch:
    push:
        paths:
            - "features/**"
    # risky... but we trust our developers :finger_crossed:
    # pull_request:
    #   paths:
    #     - "features/**"

jobs:
    make_salad:
        name: Cucumber tests
        strategy:
            fail-fast: false
            matrix:
                os: [ubuntu-latest, windows-latest]
                # We only test LTS for now
                node-version: [20]

        runs-on: ${{ matrix.os }}

        steps:
            - uses: actions/checkout@v4

            - name: Use Node.js ${{ matrix.node-version }}
              uses: actions/setup-node@v4
              with:
                  node-version: ${{ matrix.node-version }}

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate

            - name: Activate cache for Node.js ${{ matrix.node-version }}
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            - name: Install Dependencies
              run: yarn

            - name: Run Cucumber tests
              env:
                  APIFY_CLI_DISABLE_TELEMETRY: 1
                  TEST_USER_TOKEN: ${{ secrets.APIFY_TEST_USER_API_TOKEN }}
              run: yarn test:cucumber


================================================
File: /.github/workflows/release.yaml
================================================
name: Create a release

on:
    # Trigger a stable version release via GitHub's UI, with the ability to specify the type of release.
    workflow_dispatch:
        inputs:
            release_type:
                description: Release type
                required: true
                type: choice
                default: auto
                options:
                    - auto
                    - custom
                    - patch
                    - minor
                    - major
            custom_version:
                description: The custom version to bump to (only for "custom" type)
                required: false
                type: string
                default: ""

concurrency:
    group: release
    cancel-in-progress: false

jobs:
    release_metadata:
        name: Prepare release metadata
        runs-on: ubuntu-latest
        outputs:
            version_number: ${{ steps.release_metadata.outputs.version_number }}
            tag_name: ${{ steps.release_metadata.outputs.tag_name }}
            changelog: ${{ steps.release_metadata.outputs.changelog }}
            release_notes: ${{ steps.release_metadata.outputs.release_notes }}
        steps:
            - uses: apify/workflows/git-cliff-release@main
              name: Prepare release metadata
              id: release_metadata
              with:
                  release_type: ${{ inputs.release_type }}
                  custom_version: ${{ inputs.custom_version }}
                  existing_changelog_path: CHANGELOG.md

    wait_for_checks:
        name: Wait for code checks to pass
        runs-on: ubuntu-latest
        steps:
            - uses: lewagon/wait-on-check-action@v1.3.4
              with:
                  ref: ${{ github.ref }}
                  repo-token: ${{ secrets.GITHUB_TOKEN }}
                  check-regexp: (Build & Test .*|Test Python template support|Lint|Docs build)
                  wait-interval: 5

    update_changelog:
        needs: [release_metadata, wait_for_checks]
        name: Update changelog
        runs-on: ubuntu-latest
        outputs:
            changelog_commitish: ${{ steps.commit.outputs.commit_long_sha || github.sha }}

        steps:
            - name: Checkout repository
              uses: actions/checkout@v4
              with:
                  token: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}

            - name: Use Node.js 22
              uses: actions/setup-node@v4
              with:
                  node-version: 22

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate

            - name: Activate cache for Node.js 22
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            - name: Update package version in package.json
              run: yarn version ${{ needs.release_metadata.outputs.version_number }}

            - name: Update README
              run: yarn pack

            - name: Update CHANGELOG.md
              uses: DamianReeves/write-file-action@master
              with:
                  path: CHANGELOG.md
                  write-mode: overwrite
                  contents: ${{ needs.release_metadata.outputs.changelog }}

            - name: Format
              run: yarn format:fix

            - name: Commit changes
              id: commit
              uses: EndBug/add-and-commit@v9
              with:
                  author_name: Apify Release Bot
                  author_email: noreply@apify.com
                  message: "chore(release): Update changelog and package version [skip ci]"

    create_github_release:
        name: Create github release
        needs: [release_metadata, update_changelog]
        runs-on: ubuntu-latest
        env:
            GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        steps:
            - name: Create release
              uses: softprops/action-gh-release@v2
              with:
                  tag_name: ${{ needs.release_metadata.outputs.tag_name }}
                  name: ${{ needs.release_metadata.outputs.version_number }}
                  target_commitish: ${{ needs.update_changelog.outputs.changelog_commitish }}
                  body: ${{ needs.release_metadata.outputs.release_notes }}

    publish_to_npm:
        name: Publish to NPM
        needs: [update_changelog]
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v4
              with:
                  ref: ${{ needs.update_changelog.changelog_commitish }}

            - name: Use Node.js 22
              uses: actions/setup-node@v4
              with:
                  node-version: 22
                  registry-url: https://registry.npmjs.org

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate

            - name: Activate cache for Node.js 22
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            - name: Install dependencies
              run: yarn

            - name: Build module
              run: yarn build

            - name: Pack with yarn
              run: yarn pack

            - name: Publish to NPM
              run: |
                  # `yarn npm publish` does not currently support --provenance: https://github.com/yarnpkg/berry/issues/5430
                  npm publish package.tgz --provenance --access public
              env:
                  NODE_AUTH_TOKEN: ${{ secrets.APIFY_SERVICE_ACCOUNT_NPM_TOKEN }}

    update_homebrew_formula:
        name: Update Homebrew Formula
        needs: [publish_to_npm]
        runs-on: ubuntu-latest
        steps:
            - name: Checkout repository
              uses: actions/checkout@v4

            - name: Set git identity
              run: |
                  git config --global user.name 'Apify Service Account'
                  git config --global user.email 'apify-service-account@users.noreply.github.com'

            - name: Set up Homebrew
              uses: Homebrew/actions/setup-homebrew@master

            # It can happen that the updated package version is not available right after the `npm publish` command finishes
            # Try waiting 3 minutes until the updated package version is available
            - name: Wait for updated package to be available on NPM
              run: |
                  PACKAGE_VERSION=`node -p "require('./package.json').version"`
                  PACKAGE_DEFINITION_URL="https://registry.npmjs.org/apify-cli/${PACKAGE_VERSION}"

                  for _i in {1..30}; do
                      curl -sf "${PACKAGE_DEFINITION_URL}" &> /dev/null && exit 0;
                      echo "Package 'apify-cli' version '${PACKAGE_VERSION}' is not available yet, will retry in 10 seconds."
                      sleep 10;
                  done
                  curl -sf "${PACKAGE_DEFINITION_URL}" &> /dev/null || exit 1;

            - name: Update Homebrew formula in apify/homebrew-tap repo
              run: |
                  PACKAGE_VERSION=`node -p "require('./package.json').version"`
                  gh workflow run update_formula.yaml --repo apify/homebrew-tap --field package=apify-cli --field version=$PACKAGE_VERSION
              env:
                  GH_TOKEN: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}

            - name: Send PR with formula update to homebrew/homebrew-core repo
              run: |
                  PACKAGE_VERSION=`node -p "require('./package.json').version"`
                  brew tap --force homebrew/core
                  brew bump-formula-pr apify-cli \
                      --version ${PACKAGE_VERSION} \
                      --no-browse \
                      --message "Automatic update of the \`apify-cli\` formula.

                      CC @B4nan @vladfrangu"
              env:
                  HOMEBREW_GITHUB_API_TOKEN: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}


================================================
File: /.github/workflows/issue_labeling.yaml
================================================
name: Update new issue

on:
    issues:
        types:
            - opened

jobs:
    label_issues:
        name: Label issues
        runs-on: ubuntu-latest
        permissions:
            issues: write

        steps:
            # Add the "t-tooling" label to all new issues
            - uses: actions/github-script@v7
              with:
                  script: |
                      github.rest.issues.addLabels({
                        issue_number: context.issue.number,
                        owner: context.repo.owner,
                        repo: context.repo.repo,
                        labels: ["t-tooling"]
                      })


================================================
File: /.github/workflows/pre_release.yaml
================================================
name: Create a pre-release

on:
    # Push to master will deploy a beta version
    push:
        branches:
            - master
        tags-ignore:
            - "**" # Ignore all tags to prevent duplicate builds when tags are pushed.

concurrency:
    group: release
    cancel-in-progress: false

jobs:
    release_metadata:
        if: "!startsWith(github.event.head_commit.message, 'docs') && !startsWith(github.event.head_commit.message, 'ci') && startsWith(github.repository, 'apify/')"
        name: Prepare release metadata
        runs-on: ubuntu-latest
        outputs:
            version_number: ${{ steps.release_metadata.outputs.version_number }}
            changelog: ${{ steps.release_metadata.outputs.changelog }}
        steps:
            - uses: apify/workflows/git-cliff-release@main
              name: Prepare release metadata
              id: release_metadata
              with:
                  release_type: prerelease
                  existing_changelog_path: CHANGELOG.md

    wait_for_checks:
        name: Wait for code checks to pass
        runs-on: ubuntu-latest
        steps:
            - uses: lewagon/wait-on-check-action@v1.3.4
              with:
                  ref: ${{ github.ref }}
                  repo-token: ${{ secrets.GITHUB_TOKEN }}
                  check-regexp: (Build & Test .*|Test Python template support|Lint|Docs build)
                  wait-interval: 5

    update_changelog:
        needs: [release_metadata, wait_for_checks]
        name: Update changelog
        runs-on: ubuntu-latest
        outputs:
            changelog_commitish: ${{ steps.commit.outputs.commit_long_sha || github.sha }}
        steps:
            - name: Checkout repository
              uses: actions/checkout@v4
              with:
                  token: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}

            - name: Use Node.js 22
              uses: actions/setup-node@v4
              with:
                  node-version: 22
                  registry-url: https://registry.npmjs.org

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate
                  git update-index --assume-unchanged .yarnrc.yml

            - name: Activate cache for Node.js 22
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            # - name: Update package version in package.json
            #   run: yarn version ${{ needs.release_metadata.outputs.version_number }}

            - name: Update CHANGELOG.md
              uses: DamianReeves/write-file-action@master
              with:
                  path: CHANGELOG.md
                  write-mode: overwrite
                  contents: ${{ needs.release_metadata.outputs.changelog }}

            - name: Format
              run: yarn && yarn format:fix

            - name: Commit changes
              id: commit
              uses: EndBug/add-and-commit@v9
              with:
                  author_name: Apify Release Bot
                  author_email: noreply@apify.com
                  message: "chore(release): Update changelog and package version [skip ci]"

    publish_to_npm:
        name: Publish to NPM
        needs: [update_changelog]
        runs-on: ubuntu-latest

        # Required for --provenances to work
        permissions:
            id-token: write

        steps:
            - uses: actions/checkout@v4
              with:
                  ref: ${{ needs.update_changelog.changelog_commitish }}

            - name: Use Node.js 22
              uses: actions/setup-node@v4
              with:
                  node-version: 22
                  registry-url: https://registry.npmjs.org

            - name: Enable corepack
              run: |
                  corepack enable
                  corepack prepare yarn@stable --activate

            - name: Activate cache for Node.js 22
              uses: actions/setup-node@v4
              with:
                  cache: yarn

            - name: Install dependencies
              run: yarn

            # Check version consistency and increment pre-release version number for beta only.
            - name: Bump pre-release version
              run: yarn tsx ./.github/scripts/before-beta-release.ts

            - name: Build module
              run: yarn build

            - name: Pack with yarn
              run: yarn pack

            - name: Publish to NPM
              run: |
                  # `yarn npm publish` does not currently support --provenance: https://github.com/yarnpkg/berry/issues/5430
                  npm publish package.tgz --provenance --access public --tag beta
              env:
                  NODE_AUTH_TOKEN: ${{ secrets.APIFY_SERVICE_ACCOUNT_NPM_TOKEN }}


================================================
File: /.github/hooks/pre-commit
================================================
#!/bin/sh

yarn lint-staged


================================================
File: /.github/CODEOWNERS
================================================
# Documentation codeowner

* @B4nan @vladfrangu

/docs/*.md @TC-MO
/docs/*.mdx @TC-MO
/docs/changelog.md


================================================
File: /renovate.json
================================================
{
	"extends": ["config:base", ":semanticCommitTypeAll(chore)"],
	"pinVersions": false,
	"separateMajorMinor": false,
	"dependencyDashboard": false,
	"semanticCommits": "enabled",
	"lockFileMaintenance": {
		"enabled": true,
		"schedule": ["before 2am"],
		"automerge": true,
		"automergeType": "branch"
	},
	"constraints": {
		"npm": "^10.0.0"
	},
	"packageRules": [
		{
			"matchUpdateTypes": ["patch", "minor"],
			"matchCurrentVersion": "!/^0/",
			"groupName": "patch/minor dependencies",
			"groupSlug": "all-non-major",
			"automerge": true,
			"automergeType": "branch"
		}
	],
	"schedule": ["every weekday"]
}


================================================
File: /tsconfig.eslint.json
================================================
{
	"extends": "./tsconfig.json",
	"compilerOptions": {
		"allowJs": true
	},
	"include": [
		"src",
		"scripts",
		"bin",
		"vitest.config.ts",
		"test",
		".yarn/plugins/postinstallDev.cjs",
		"features/**/*.ts"
	]
}


================================================
File: /biome.json
================================================
{
	"formatter": {
		"ignore": [
			"website/**",
			"dist/**",
			"test/__setup__/input-schemas/*.json",
			"package.json"
		],
		"formatWithErrors": true
	},
	"javascript": {
		"formatter": {
			"quoteStyle": "single",
			"semicolons": "always",
			"trailingCommas": "all",
			"lineWidth": 120,
			"indentStyle": "tab",
			"indentWidth": 4,
			"quoteProperties": "preserve",
			"lineEnding": "lf"
		}
	},
	"linter": {
		"enabled": false
	}
}


================================================
File: /.eslintrc.json
================================================
{
	"extends": ["@apify/ts", "prettier"],
	"parserOptions": {
		"project": "./tsconfig.eslint.json",
		"ecmaVersion": 2022
	},
	"rules": {
		"no-console": "off"
	}
}


================================================
File: /test/__setup__/hooks/useAuthSetup.ts
================================================
import { rm } from 'node:fs/promises';

import { cryptoRandomObjectId } from '@apify/utilities';

import { GLOBAL_CONFIGS_FOLDER } from '../../../src/lib/consts.js';

export interface UseAuthSetupOptions {
	/**
	 * If true, the created auth data will be automatically removed after the test suite.
	 * @default true
	 */
	cleanup?: boolean;
	/**
	 * If true, there will be a new auth state per test instead of per suite.
	 * @default true
	 */
	perTest?: boolean;
}

// Keep in sync with GLOBAL_CONFIGS_FOLDER in consts.ts
const envVariable = '__APIFY_INTERNAL_TEST_AUTH_PATH__';

/**
 * A hook that allows each test to have a unique auth setup.
 */
export function useAuthSetup({ cleanup, perTest }: UseAuthSetupOptions = { cleanup: true, perTest: true }) {
	const random = cryptoRandomObjectId(12);

	const envValue = () => (perTest ? cryptoRandomObjectId(12) : random);

	const before = perTest ? beforeEach : beforeAll;
	const after = perTest ? afterEach : afterAll;

	before(() => {
		vitest.stubEnv(envVariable, envValue());
	});

	after(async () => {
		if (cleanup) {
			await rm(GLOBAL_CONFIGS_FOLDER(), { recursive: true, force: true });
		}

		vitest.unstubAllEnvs();
	});
}


================================================
File: /test/__setup__/hooks/useProcessMock.ts
================================================
import { MockSTDIN, stdin as fstdin } from 'mock-stdin';

interface ProcessMockOptions {
	cwdMock: () => string;
	mockStdin?: boolean;
}

export function useProcessMock({ cwdMock, mockStdin }: ProcessMockOptions) {
	let actualStdin: unknown = process.stdin;

	if (mockStdin) {
		actualStdin = fstdin();
	}

	vitest.doMock('node:process', async () => {
		const actual = await import('node:process');

		return {
			...actual,
			cwd: cwdMock,
			stdin: actualStdin,
			default: {
				...actual,
				cwd: cwdMock,
				stdin: actualStdin,
			},
		};
	});

	vitest.doMock('process', async () => {
		const actual = await import('process');

		return {
			...actual,
			cwd: cwdMock,
			stdin: actualStdin,
			default: {
				...actual,
				cwd: cwdMock,
				stdin: actualStdin,
			},
		};
	});

	const processCwdSpy = vitest.spyOn(process, 'cwd');
	processCwdSpy.mockImplementation(cwdMock);

	return {
		stdin: actualStdin as MockSTDIN,
	};
}


================================================
File: /test/__setup__/hooks/withRetries.ts
================================================
export async function withRetries<T extends () => unknown>(func: T, retries: number = 3, delay: number = 1000) {
	let result;
	for (let i = 0; i < retries; i++) {
		try {
			result = await func();
			break;
		} catch (err) {
			if (i === retries - 1) {
				throw err;
			}

			await new Promise((resolve) => setTimeout(resolve, delay));
		}
	}

	return result;
}


================================================
File: /test/__setup__/hooks/useConsoleSpy.ts
================================================
import { MockInstance } from 'vitest';

export function useConsoleSpy() {
	let logSpy!: MockInstance<Parameters<(typeof console)['log']>, void>;
	let errorSpy!: MockInstance<Parameters<(typeof console)['error']>, void>;

	const logMessages = {
		log: [] as string[],
		error: [] as string[],
	};

	vitest.setConfig({ restoreMocks: false });

	beforeEach(() => {
		logSpy = vitest.spyOn(console, 'log').mockImplementation((...args) => {
			logMessages.log.push(args.map(String).join(' '));
		});

		errorSpy = vitest.spyOn(console, 'error').mockImplementation((...args) => {
			logMessages.error.push(args.map(String).join(' '));
		});
	});

	return {
		get logSpy() {
			return logSpy;
		},
		get errorSpy() {
			return errorSpy;
		},
		logMessages,
	};
}


================================================
File: /test/__setup__/hooks/useTempPath.ts
================================================
import { mkdir } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { MockSTDIN } from 'mock-stdin';

import { useProcessMock } from './useProcessMock.js';
import { rimrafPromised } from '../../../src/lib/files.js';

export interface UseTempPathOptions {
	/**
	 * If true, the temp path will be created if it does not exist.
	 * @default true
	 */
	create: boolean;

	/**
	 * If true, the temp path will be removed after the test.
	 * @default true
	 */
	remove: boolean;

	/**
	 * If true, process.cwd() will be set to the temp path.
	 * @default false
	 */
	cwd: boolean;

	/**
	 * If true, the mocked process.cwd will point to the parent folder of the temp path.
	 * This will also change how the temp path is created: it will only create the parent folder, not the nested folder!
	 * @default false
	 */
	cwdParent: boolean;

	/**
	 * If true, the stdin will also be mocked.
	 */
	withStdinMock?: boolean;
}

export function useTempPath(
	path: string,
	{ create, remove, cwd, cwdParent, withStdinMock }: UseTempPathOptions = {
		create: true,
		remove: true,
		cwd: false,
		cwdParent: false,
		withStdinMock: false,
	},
) {
	const tmpPath = join(fileURLToPath(import.meta.url), '..', '..', '..', 'tmp', path);
	const cwdPath = cwdParent ? join(fileURLToPath(import.meta.url), '..', '..', '..', 'tmp') : tmpPath;

	let usedCwd = cwdPath;

	let mockedStdin = process.stdin as unknown as MockSTDIN;

	if (cwd) {
		const cwdMock = () => usedCwd;

		const { stdin } = useProcessMock({ cwdMock, mockStdin: withStdinMock });
		mockedStdin = stdin;
	}

	return {
		tmpPath,
		joinPath: (...paths: string[]) => join(tmpPath, ...paths),
		joinCwdPath: (...paths: string[]) => join(usedCwd, ...paths),
		beforeAllCalls: async () => {
			if (create) {
				if (cwdParent) {
					await mkdir(cwdPath, { recursive: true });
				} else {
					await mkdir(tmpPath, { recursive: true });
				}
			}

			// Always reset the usedCwd to the expected initial state
			usedCwd = cwdPath;
		},
		afterAllCalls: async () => {
			if (remove) {
				await rimrafPromised(tmpPath);
			}
		},

		toggleCwdBetweenFullAndParentPath: () => {
			usedCwd = usedCwd === cwdPath ? tmpPath : cwdPath;
		},

		forceNewCwd: (newCwd: string) => {
			usedCwd = join(cwdPath, newCwd);
		},

		stdin: mockedStdin,
	};
}


================================================
File: /test/__setup__/config.ts
================================================
import { ApifyClient } from 'apify-client';

import { getApifyClientOptions } from '../../src/lib/utils.js';

const { TEST_USER_TOKEN: ENV_TEST_USER_TOKEN } = process.env;
export const TEST_USER_BAD_TOKEN = 'badToken';

if (!ENV_TEST_USER_TOKEN) {
	throw Error('You must configure "TEST_USER_TOKEN" environment variable to run tests!');
}

export const testUserClient = new ApifyClient(getApifyClientOptions(ENV_TEST_USER_TOKEN));

export const badUserClient = new ApifyClient(getApifyClientOptions(TEST_USER_BAD_TOKEN));

export const TEST_USER_TOKEN = ENV_TEST_USER_TOKEN;


================================================
File: /test/__setup__/build-utils.ts
================================================
import { ACTOR_JOB_STATUSES } from '@apify/consts';
import { ApifyClient } from 'apify-client';

/**
 * Waits for the build to finish
 */
export const waitForBuildToFinish = async (client: ApifyClient, buildId: string) => {
	while (true) {
		const build = await client.build(buildId).get();
		if (build!.status !== (ACTOR_JOB_STATUSES.RUNNING as unknown)) return build;
		await new Promise((resolve) => setTimeout(resolve, 2500));
	}
};

/**
 * Waits for build to finish with timeout, throws an error on timeout
 */
export const waitForBuildToFinishWithTimeout = async (client: ApifyClient, buildId: string, timeoutSecs = 60) => {
	const buildPromise = waitForBuildToFinish(client, buildId);
	const timeoutPromise = new Promise((resolve) => setTimeout(() => resolve(false), timeoutSecs * 1000));
	const result = await Promise.race([buildPromise, timeoutPromise]);
	if (!result) throw new Error(`Timed out after ${timeoutSecs} seconds`);
};


================================================
File: /test/__setup__/test-data/input-file.json
================================================
{
	"hello": "world"
}


================================================
File: /test/__setup__/input-schemas/prefills.json
================================================
{
  "title": "Defaults",
  "description": "Ensures defaults also get filled into the input",
  "type": "object",
  "schemaVersion": 1,
  "properties": {
    "awesome": {
      "title": "Are you awesome",
      "type": "boolean",
      "description": "yesnt",
      "editor": "checkbox"
    },
    "help": {
      "title": "optional",
      "type": "string",
      "description": "A message, stop looking in these files",
      "prefill": "this_maze_is_not_meant_for_you",
      "editor": "textfield"
    }
  },
  "required": [
    "awesome"
  ]
}


================================================
File: /test/__setup__/input-schemas/missing-required-property.json
================================================
{
  "title": "required",
  "description": "Ensures cli throws when required fields are missing",
  "type": "object",
  "schemaVersion": 1,
  "properties": {
    "awesome": {
      "title": "Are you awesome",
      "type": "boolean",
      "description": "yesnt",
      "editor": "checkbox"
    }
  },
  "required": [
    "awesome"
  ]
}


================================================
File: /test/__setup__/input-schemas/invalid.json
================================================
{
	"title": "Google SERP crawler input",
	"description": "Invalid schema - nonexisting editor.",
	"type": "object",
	"schemaVersion": 1,
	"properties": {
		"queries": {
			"title": "Queries or search URLs",
			"type": "string",
			"description": "Enter here your queries or search URLs, one item per line.",
			"prefill": "Hotels in Prague\nRestaurants in Prague\nhttps://www.google.com/search?q=acoomodation&oq=acoomodation&aqs=chrome..69i57j0l5.1637j0j1&sourceid=chrome&ie=UTF-8",
			"editor": "spaceEditor"
		}
	},
	"required": ["queries"]
}


================================================
File: /test/__setup__/input-schemas/defaults.json
================================================
{
  "title": "Defaults",
  "description": "Ensures defaults also get filled into the input",
  "type": "object",
  "schemaVersion": 1,
  "properties": {
    "awesome": {
      "title": "Are you awesome",
      "type": "boolean",
      "description": "yesnt",
      "editor": "checkbox"
    },
    "help": {
      "title": "optional",
      "type": "string",
      "description": "A message, stop looking in these files",
      "default": "this_maze_is_not_meant_for_you",
      "editor": "textfield"
    }
  },
  "required": [
    "awesome"
  ]
}


================================================
File: /test/__setup__/input-schemas/unparsable.json
================================================
{
	"title": "Google SERP crawler input",
	"description": "Invalid schema - nonexisting editor.",
	"type": "object",
	"schemaVersion": 1,
	"properties": {
		"queries": {
			"title": "Queries or search URLs",
			"type": "string",
			"description": "Enter here your queries or search URLs, one item per line.",
			"prefill": "Hotels in Prague\nRestaurants in Prague\nhttps://www.google.com/search?q=acoomodation&oq=acoomodation&aqs=chrome..69i57j0l5.1637j0j1&sourceid=chrome&ie=UTF-8",
			"editor": "spaceEditor"
		}
	},
	"required": ["queries"
}


================================================
File: /test/__setup__/input-schemas/valid.json
================================================
{
	"title": "Google SERP crawler input",
	"description": "Define the Google search query using parameters below. You can scrape the data using specific language, country and location UUID.",
	"type": "object",
	"schemaVersion": 1,
	"properties": {
		"queries": {
			"title": "Queries or search URLs",
			"type": "string",
			"description": "Enter here your queries or search URLs, one item per line.",
			"prefill": "Hotels in Prague\nRestaurants in Prague\nhttps://www.google.com/search?q=acoomodation&oq=acoomodation&aqs=chrome..69i57j0l5.1637j0j1&sourceid=chrome&ie=UTF-8",
			"editor": "textarea"
		},
		"locationUule": {
			"title": "Uule location code",
			"type": "string",
			"description": "Enter [UULE](https://moz.com/ugc/geolocation-the-ultimate-tip-to-emulate-local-search) location code you want to use for geo spacious search results. This setting is not applied to search URLs entered above but only to text queries.",
			"editor": "textfield"
		},
		"resultsNum": {
			"title": "Results number per page",
			"type": "integer",
			"description": "Enter how many results per page you want to query. Maximum is 100.",
			"default": 10,
			"maximum": 100,
			"minimum": 1
		},
		"maxPagesPerQuery": {
			"title": "Max pages per query",
			"type": "integer",
			"description": "Enter up to how many results pages you want to get for one query.",
			"default": 1,
			"minimum": 1
		},
		"maxConcurrency": {
			"title": "Max concurrency",
			"type": "integer",
			"description": "Enter the maximum concurrency for this crawler. Higher number will give you results faster but will burn your available proxies faster on the other hand.",
			"default": 10,
			"maximum": 100,
			"minimum": 1
		},
		"deviceType": {
			"title": "Device type",
			"type": "string",
			"description": "Select device type you want to use.",
			"editor": "select",
			"default": "DESKTOP",
			"enum": ["DESKTOP", "MOBILE"],
			"enumTitles": ["Desktop", "Mobile"]
		},
		"saveHtml": {
			"title": "Save HTML",
			"type": "boolean",
			"description": "If checked then HTML of Google search results page will be stored in results.",
			"default": false,
			"groupCaption": "Options",
			"groupDescription": "Various options for this Actor"
		}
	},
	"required": ["queries"]
}


================================================
File: /test/crawlee/commands/run.test.ts
================================================
import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

import { captureOutput } from '@oclif/test';

import { getLocalKeyValueStorePath } from '../../../src/lib/utils.js';
import { useTempPath } from '../../__setup__/hooks/useTempPath.js';

const actorName = 'run-my-crawlee';
const pathToDefaultsInputSchema = fileURLToPath(
	new URL('../../__setup__/input-schemas/defaults.json', import.meta.url),
);

const overridenMainJs = `
import { Actor } from 'apify';

await Actor.init();

const input = await Actor.getInput();
await Actor.setValue('OUTPUT', input);

await Actor.exit();
`;

const originalInput = JSON.stringify({ awesome: true });
const originalInputWithExtraField = JSON.stringify({ awesome: true, extra: 'field' });

const { beforeAllCalls, afterAllCalls, joinPath, toggleCwdBetweenFullAndParentPath } = useTempPath(actorName, {
	create: true,
	remove: true,
	cwd: true,
	cwdParent: true,
});

const { CreateCommand } = await import('../../../src/commands/create.js');
const { RunCommand } = await import('../../../src/commands/run.js');

describe('apify run', () => {
	let inputPath: string;
	let outputPath: string;

	beforeAll(async () => {
		await beforeAllCalls();

		await CreateCommand.run([actorName, '--template', 'project_cheerio_crawler_js'], import.meta.url);
		toggleCwdBetweenFullAndParentPath();

		await writeFile(joinPath('src/main.js'), overridenMainJs);
		await writeFile(joinPath('.actor/input_schema.json'), await readFile(pathToDefaultsInputSchema, 'utf8'));

		inputPath = joinPath(getLocalKeyValueStorePath(), 'INPUT.json');
		outputPath = joinPath(getLocalKeyValueStorePath(), 'OUTPUT.json');
	});

	afterAll(async () => {
		await afterAllCalls();
	});

	it('throws when required field is not provided', async () => {
		await writeFile(inputPath, '{}');

		const { error } = await captureOutput(async () => RunCommand.run([], import.meta.url));

		expect(error).toBeDefined();
		expect(error!.message).toMatch(/Field awesome is required/i);
	});

	it('prefills input with defaults', async () => {
		await writeFile(inputPath, originalInput);

		await RunCommand.run([], import.meta.url);

		const output = JSON.parse(await readFile(outputPath, 'utf8'));
		expect(output).toStrictEqual({ awesome: true, help: 'this_maze_is_not_meant_for_you' });
	});

	it('should restore the original input file after run', async () => {
		await writeFile(inputPath, originalInputWithExtraField);

		await RunCommand.run([], import.meta.url);

		const input = JSON.parse(await readFile(inputPath, 'utf8'));
		expect(input).toStrictEqual({ awesome: true, extra: 'field' });

		const output = JSON.parse(await readFile(outputPath, 'utf8'));
		expect(output).toStrictEqual({ awesome: true, help: 'this_maze_is_not_meant_for_you', extra: 'field' });
	});
});


================================================
File: /test/python_support.test.ts
================================================
import { existsSync, writeFileSync } from 'node:fs';
import { rm } from 'node:fs/promises';

import { loadJsonFileSync } from 'load-json-file';

import { useTempPath } from './__setup__/hooks/useTempPath.js';
import { detectPythonVersion, getLocalKeyValueStorePath } from '../src/lib/utils.js';

const actorName = 'my-python-actor';
const PYTHON_START_TEMPLATE_ID = 'python-start';
const { beforeAllCalls, afterAllCalls, joinPath, tmpPath, toggleCwdBetweenFullAndParentPath } = useTempPath(actorName, {
	create: true,
	remove: true,
	cwd: true,
	cwdParent: true,
});

const { CreateCommand } = await import('../src/commands/create.js');
const { RunCommand } = await import('../src/commands/run.js');

describe('Python support [python]', () => {
	beforeAll(async () => {
		await beforeAllCalls();
	});

	afterAll(async () => {
		await afterAllCalls();
	});

	it('Python templates work [python]', { timeout: 120_000 }, async () => {
		const pythonVersion = detectPythonVersion('.');
		// Don't fail this test when Python is not installed (it will be installed in the right CI workflow)
		if (!pythonVersion && !process.env.CI) {
			console.log('Skipping Python template test since Python is not installed');
			return;
		}

		if (existsSync(tmpPath)) {
			// Remove the tmp path if it exists
			await rm(tmpPath, { recursive: true, force: true });
		}

		await CreateCommand.run([actorName, '--template', PYTHON_START_TEMPLATE_ID], import.meta.url);

		// Check file structure
		expect(existsSync(tmpPath)).toBeTruthy();

		expect(existsSync(joinPath('.venv'))).toBeTruthy();
		expect(existsSync(joinPath('requirements.txt'))).toBeTruthy();

		const expectedOutput = {
			hello: 'world',
		};

		const actorCode = `from apify import Actor
async def main():
    async with Actor:
        await Actor.set_value('OUTPUT', ${JSON.stringify(expectedOutput)})
`;
		writeFileSync(joinPath('src', 'main.py'), actorCode, { flag: 'w' });

		toggleCwdBetweenFullAndParentPath();

		await RunCommand.run([], import.meta.url);

		// Check Actor output
		const actorOutputPath = joinPath(getLocalKeyValueStorePath(), 'OUTPUT.json');
		const actorOutput = loadJsonFileSync(actorOutputPath);
		expect(actorOutput).toStrictEqual(actorOutput);
	});
});


================================================
File: /test/lib/actor.test.ts
================================================
import { APIFY_ENV_VARS } from '@apify/consts';
import { ApifyClient } from 'apify-client';

import { getApifyStorageClient } from '../../src/lib/actor.js';

beforeAll(() => {
	vitest.stubEnv(APIFY_ENV_VARS.IS_AT_HOME, 'true');
	vitest.stubEnv(APIFY_ENV_VARS.TOKEN, 'token for sure');
});

afterAll(() => {
	vitest.unstubAllEnvs();
});

describe('getApifyStorageClient should return a cloud instance when APIFY_IS_AT_HOME is set', () => {
	it('should return a cloud instance', async () => {
		await expect(getApifyStorageClient()).resolves.toBeInstanceOf(ApifyClient);
	});
});


================================================
File: /test/utils.test.ts
================================================
import { existsSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

import { useTempPath } from './__setup__/hooks/useTempPath.js';
import { withRetries } from './__setup__/hooks/withRetries.js';
import { execWithLog } from '../src/lib/exec.js';
import { ensureFolderExistsSync } from '../src/lib/files.js';
import { argsToCamelCase, createActZip, getActorLocalFilePaths } from '../src/lib/utils.js';

const TEST_DIR = 'my-test-dir';
const FOLDERS = ['my_test', 'my_test/test_in_test', 'my_next_test', '.dot_test'];
const FOLDERS_TO_IGNORE = ['test_to_ignore', 'my_test/this_ignore'];
const FILES = [
	'main.js',
	'my_module.js',
	'next_module.js',
	'my_test/test.js',
	'my_test/test_in_test/test.js',
	'my_next_test/test.js',
	'.dot_test/test.js',
];
const FILES_IN_IGNORED_DIR = ['test_to_ignore/in_test_ignore.js'];
const FILES_TO_IGNORE = ['ignored_module.js'];

describe('Utils', () => {
	describe('argsToCamelCase()', () => {
		it('should convert object', () => {
			const object = {
				'my-att': 'value',
				'my-attr-test': 'secondValue',
				'user-id': 'd7H9khHg',
				token: 'Ad7H9khHgd7H9khHg',
			};
			const expected = {
				myAtt: 'value',
				myAttrTest: 'secondValue',
				userId: 'd7H9khHg',
				token: 'Ad7H9khHgd7H9khHg',
			};
			const convertedObject = argsToCamelCase(object);
			expect(expected).to.be.eql(convertedObject);
		});
	});

	describe('createActZip()', () => {
		const { tmpPath, joinPath, beforeAllCalls, afterAllCalls } = useTempPath(TEST_DIR, {
			create: true,
			remove: true,
			cwd: false,
			cwdParent: false,
		});

		beforeAll(async () => {
			await beforeAllCalls();

			FOLDERS.concat(FOLDERS_TO_IGNORE).forEach((folder) => {
				ensureFolderExistsSync(tmpPath, folder);
			});

			FILES.concat(FILES_TO_IGNORE, FILES_IN_IGNORED_DIR).forEach((file) =>
				writeFileSync(joinPath(file), Math.random().toString(36).substring(7), { flag: 'w' }),
			);

			const toIgnore = FOLDERS_TO_IGNORE.concat(FILES_TO_IGNORE).join('\n');
			writeFileSync(joinPath('.gitignore'), toIgnore, { flag: 'w' });
		});

		afterAll(async () => {
			await afterAllCalls();
		});

		it('should create zip without files in .gitignore', async () => {
			const zipName = joinPath('test.zip');
			const tempFolder = joinPath('unzip_temp');
			ensureFolderExistsSync(tmpPath, 'unzip_temp');
			const pathsToZip = await getActorLocalFilePaths(tmpPath);
			await createActZip(zipName, pathsToZip, tmpPath);

			// Unzip with same command as on Apify worker
			// Add in some retries for when the FS is slow to update
			await withRetries(
				async () => {
					await execWithLog('unzip', ['-oq', zipName, '-d', tempFolder]);
				},
				3,
				20,
			);

			FOLDERS.forEach((folder) => expect(existsSync(join(tempFolder, folder))).toBeTruthy());
			FOLDERS_TO_IGNORE.forEach((folder) => expect(existsSync(join(tempFolder, folder))).toBeFalsy());
			FILES.forEach((file) => expect(existsSync(join(tempFolder, file))).toBeTruthy());
			FILES_IN_IGNORED_DIR.concat(FILES_TO_IGNORE).forEach((file) =>
				expect(existsSync(join(tempFolder, file))).toBeFalsy(),
			);
		});
	});
});


================================================
File: /test/secrets.test.ts
================================================
import { replaceSecretsValue } from '../src/lib/secrets.js';

describe('Secrets', () => {
	describe('replaceSecretsValue()', () => {
		it('should work', () => {
			const spy = vitest.spyOn(console, 'error');

			const secrets = {
				myProdToken: 'mySecretToken',
				mongoUrl: 'mongo://bla@bla:supermongo.com:27017',
			};
			const env = {
				TOKEN: '@myProdToken',
				USER: 'jakub.drobnik@apify.com',
				MONGO_URL: '@mongoUrl',
				WARNING: '@doesNotExist',
			};
			const updatedEnv = replaceSecretsValue(env, secrets);

			expect(updatedEnv).toStrictEqual({
				TOKEN: secrets.myProdToken,
				USER: 'jakub.drobnik@apify.com',
				MONGO_URL: secrets.mongoUrl,
			});

			expect(spy).toHaveBeenCalled();
			expect(spy.mock.calls[0][0]).to.include('Warning:');
		});
	});
});


================================================
File: /test/consts.test.ts
================================================
import { INPUT_FILE_REG_EXP } from '../src/lib/consts.js';

describe('Consts', () => {
	describe('INPUT_FILE_REG_EXP', () => {
		const testValues = [
			{
				text: 'INPUT.json',
				match: true,
			},
			{
				text: 'INPUT.png',
				match: true,
			},
			{
				text: 'INPUT_.json',
				match: false,
			},
			{
				text: 'bla_INPUT.json',
				match: false,
			},
			{
				text: 'bla_bla.json',
				match: false,
			},
		];

		testValues.forEach((value) => {
			it(`should match ${value.text}`, () => {
				expect(!!value.text.match(INPUT_FILE_REG_EXP)).toEqual(value.match);
			});
		});
	});
});


================================================
File: /test/tsconfig.json
================================================
{
	"extends": "../tsconfig.json",
	"compilerOptions": {
		"types": ["vitest/globals"],
		"allowJs": true,
		"checkJs": false,
		"noEmit": true,
		"rootDir": "."
	},
	"include": ["./**/*.ts", "./**/*.js", "../src"],
	"references": [{ "path": ".." }]
}


================================================
File: /test/version_check.test.ts
================================================
import { getLatestNpmVersion } from '../src/lib/version_check.js';

describe('VersionCheck', () => {
	describe('getLatestNpmVersion()', () => {
		it('should return package version', async () => {
			const latestVersion = await getLatestNpmVersion();
			expect(latestVersion).to.match(/^\d+\.\d+\.\d+$/);
		});
	});
});


================================================
File: /test/templates.test.ts
================================================
import { fetchManifest } from '@apify/actor-templates';

describe('templates', () => {
	it('can be fetched', async () => {
		const { templates } = await fetchManifest();
		expect(Array.isArray(templates)).toBeTruthy();
		expect(templates.length).toBeGreaterThan(0);
	});
});


================================================
File: /test/commands/create.test.ts
================================================
import { existsSync } from 'node:fs';

import { KEY_VALUE_STORE_KEYS } from '@apify/consts';
import { runCommand } from '@oclif/test';
import { loadJsonFileSync } from 'load-json-file';

import { LOCAL_CONFIG_PATH } from '../../src/lib/consts.js';
import { getLocalKeyValueStorePath } from '../../src/lib/utils.js';
import { useTempPath } from '../__setup__/hooks/useTempPath.js';

const actName = 'create-my-actor';
const { beforeAllCalls, afterAllCalls, joinPath, toggleCwdBetweenFullAndParentPath, tmpPath } = useTempPath(actName, {
	create: true,
	remove: true,
	cwd: true,
	cwdParent: true,
});

const { CreateCommand } = await import('../../src/commands/create.js');

describe('apify create', () => {
	beforeEach(async () => {
		await beforeAllCalls();
	});

	afterEach(async () => {
		await afterAllCalls();
	});

	['a'.repeat(151), 'sh', 'bad_escaped'].forEach((badActorName) => {
		it(`returns error with bad Actor name ${badActorName}`, async () => {
			const { error } = await runCommand(['create', badActorName], import.meta.url);

			expect(error).toBeTruthy();
		});
	});

	it('basic template structure with empty INPUT.json', async () => {
		const ACT_TEMPLATE = 'project_empty';
		const expectedInput = {};
		await CreateCommand.run([actName, '--template', ACT_TEMPLATE, '--skip-dependency-install'], import.meta.url);

		// check files structure
		expect(existsSync(tmpPath)).toBeTruthy();

		toggleCwdBetweenFullAndParentPath();

		// Check that create command won't create the deprecated apify.json file
		// TODO: we can remove this later
		const apifyJsonPath = joinPath('apify.json');
		const actorJsonPath = joinPath(LOCAL_CONFIG_PATH);

		expect(existsSync(joinPath('package.json'))).toBeTruthy();
		expect(existsSync(apifyJsonPath)).toBeFalsy();
		expect(existsSync(actorJsonPath)).toBeTruthy();
		expect(loadJsonFileSync<{ name: string }>(actorJsonPath).name).to.be.eql(actName);
		expect(loadJsonFileSync(joinPath(getLocalKeyValueStorePath(), `${KEY_VALUE_STORE_KEYS.INPUT}.json`))).to.be.eql(
			expectedInput,
		);
	});

	it('basic template structure with prefilled INPUT.json', async () => {
		const ACT_TEMPLATE = 'getting_started_typescript';
		const expectedInput = { url: 'https://www.apify.com' };

		await CreateCommand.run([actName, '--template', ACT_TEMPLATE, '--skip-dependency-install'], import.meta.url);

		// check files structure
		expect(existsSync(tmpPath)).toBeTruthy();

		toggleCwdBetweenFullAndParentPath();

		// Check that create command won't create the deprecated apify.json file
		// TODO: we can remove this later
		const apifyJsonPath = joinPath('apify.json');
		const actorJsonPath = joinPath(LOCAL_CONFIG_PATH);

		expect(existsSync(joinPath('package.json'))).toBeTruthy();
		expect(existsSync(apifyJsonPath)).toBeFalsy();
		expect(existsSync(actorJsonPath)).toBeTruthy();
		expect(loadJsonFileSync<{ name: string }>(actorJsonPath)!.name).to.be.eql(actName);
		expect(loadJsonFileSync(joinPath(getLocalKeyValueStorePath(), `${KEY_VALUE_STORE_KEYS.INPUT}.json`))).to.be.eql(
			expectedInput,
		);
	});

	it('should skip installing optional dependencies', async () => {
		const ACT_TEMPLATE = 'project_cheerio_crawler_js';
		await CreateCommand.run([actName, '--template', ACT_TEMPLATE, '--no-optional'], import.meta.url);

		// check files structure
		expect(existsSync(tmpPath)).toBeTruthy();

		toggleCwdBetweenFullAndParentPath();

		expect(existsSync(joinPath('package.json'))).toBeTruthy();
		expect(existsSync(joinPath('node_modules'))).toBeTruthy();
		expect(existsSync(joinPath('node_modules', 'cheerio'))).toBeTruthy();
		expect(existsSync(joinPath('node_modules', 'playwright'))).toBeFalsy();
	});
});


================================================
File: /test/commands/info.test.ts
================================================
import { runCommand } from '@oclif/test';
import { loadJsonFileSync } from 'load-json-file';

import { InfoCommand } from '../../src/commands/info.js';
import { LoginCommand } from '../../src/commands/login.js';
import { AUTH_FILE_PATH } from '../../src/lib/consts.js';
import { TEST_USER_TOKEN } from '../__setup__/config.js';
import { useAuthSetup } from '../__setup__/hooks/useAuthSetup.js';

useAuthSetup();

describe('apify info', () => {
	it('should end with Error when not logged in', async () => {
		const { error } = await runCommand(['info'], import.meta.url);

		expect(error).toBeTruthy();
	});

	it('should work when logged in', async () => {
		const spy = vitest.spyOn(console, 'log');

		await LoginCommand.run(['--token', TEST_USER_TOKEN], import.meta.url);
		await InfoCommand.run([], import.meta.url);

		const userInfoFromConfig = loadJsonFileSync<{ id: string }>(AUTH_FILE_PATH());

		expect(spy).toHaveBeenCalledTimes(2);
		expect(spy.mock.calls[1][0]).to.include(userInfoFromConfig.id);
	});
});


================================================
File: /test/commands/validate-schema.test.ts
================================================
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { runCommand } from '@oclif/test';

const basePath = join(fileURLToPath(import.meta.url), '../../__setup__/input-schemas/');

describe('apify validate-schema', () => {
	it('should correctly validate schema 1', async () => {
		const { error } = await runCommand(['validate-schema', join(basePath, 'valid.json')], import.meta.url);

		expect(error).toBeFalsy();
	});

	it('should correctly validate schema 2', async () => {
		const { error } = await runCommand(['validate-schema', join(basePath, 'invalid.json')], import.meta.url);

		expect(error).toBeTruthy();
		expect(error?.message).to.contain(
			'Field schema.properties.queries.editor must be equal to one of the allowed values',
		);
	});

	it('should correctly validate schema 3', async () => {
		const { error } = await runCommand(['validate-schema', join(basePath, 'unparsable.json')], import.meta.url);

		expect(error).toBeTruthy();
		expect(error?.message).to.contain.oneOf(['Unexpected token }', "Expected ',' or ']' after array element"]);
	});

	it('should correctly validate schema 1 with alias', async () => {
		const { error } = await runCommand(['vis', join(basePath, 'valid.json')], import.meta.url);

		expect(error).toBeFalsy();
	});
});


================================================
File: /test/commands/task/run.test.ts
================================================
import { writeFileSync } from 'node:fs';
import { platform } from 'node:os';

import { cryptoRandomObjectId } from '@apify/utilities';

import { waitForBuildToFinishWithTimeout } from '../../__setup__/build-utils.js';
import { TEST_USER_TOKEN, testUserClient } from '../../__setup__/config.js';
import { useAuthSetup } from '../../__setup__/hooks/useAuthSetup.js';
import { useTempPath } from '../../__setup__/hooks/useTempPath.js';

const actName = `task-on-my-actor-${cryptoRandomObjectId(6)}-${process.version.split('.')[0]}-${platform()}`;
const taskName = `my-task-${cryptoRandomObjectId(6)}-${process.version.split('.')[0]}-${platform()}`;

useAuthSetup({ perTest: false });

const { beforeAllCalls, afterAllCalls, joinPath, toggleCwdBetweenFullAndParentPath } = useTempPath(actName, {
	create: true,
	remove: true,
	cwd: true,
	cwdParent: true,
});

const { LoginCommand } = await import('../../../src/commands/login.js');
const { CreateCommand } = await import('../../../src/commands/create.js');
const { ActorsPushCommand } = await import('../../../src/commands/actors/push.js');
const { TaskRunCommand } = await import('../../../src/commands/task/run.js');

const expectedOutput = {
	test: 'hello world!!',
};

describe('apify task run', () => {
	let actorId: string;
	let taskId: string;

	beforeAll(async () => {
		await beforeAllCalls();

		const { username } = await testUserClient.user('me').get();

		await LoginCommand.run(['--token', TEST_USER_TOKEN], import.meta.url);
		await CreateCommand.run([actName, '--template', 'project_empty', '--skip-dependency-install'], import.meta.url);

		const actCode = `
        import { Actor } from 'apify';

        Actor.main(async () => {
            await Actor.setValue('OUTPUT', await Actor.getInput());
            console.log('Done.');
        });
        `;

		writeFileSync(joinPath('src/main.js'), actCode, { flag: 'w' });

		toggleCwdBetweenFullAndParentPath();
		await ActorsPushCommand.run(['--no-prompt', '--force'], import.meta.url);

		actorId = `${username}/${actName}`;

		// Build must finish before doing `apify call`, otherwise we would get nonexisting build with "LATEST" tag error.
		const builds = await testUserClient.actor(actorId).builds().list();
		const lastBuild = builds.items.pop();
		await waitForBuildToFinishWithTimeout(testUserClient, lastBuild!.id);

		// Make a task for this actor
		const task = await testUserClient.tasks().create({
			actId: actorId,
			name: taskName,
			input: expectedOutput,
		});

		taskId = `${username}/${task.name}`;
	});

	afterAll(async () => {
		await testUserClient.task(taskId).delete();
		await testUserClient.actor(actorId).delete();

		await afterAllCalls();
	});

	it('should work with just the task name', async () => {
		await expect(TaskRunCommand.run([taskName], import.meta.url)).resolves.toBeUndefined();

		const taskClient = testUserClient.task(taskId);
		const runs = await taskClient.runs().list();
		const lastRun = runs.items.pop();
		const lastRunDetail = await testUserClient.run(lastRun!.id).get();
		const output = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('OUTPUT');

		expect(expectedOutput).toStrictEqual(output!.value);
	});

	it('should work with the full name', async () => {
		await expect(TaskRunCommand.run([taskId], import.meta.url)).resolves.toBeUndefined();

		const taskClient = testUserClient.task(taskId);
		const runs = await taskClient.runs().list();
		const lastRun = runs.items.pop();
		const lastRunDetail = await testUserClient.run(lastRun!.id).get();
		const output = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('OUTPUT');

		expect(expectedOutput).toStrictEqual(output!.value);
	});
});


================================================
File: /test/commands/call.test.ts
================================================
import { readFileSync, writeFileSync } from 'node:fs';
import { platform } from 'node:os';
import { fileURLToPath } from 'node:url';

import { cryptoRandomObjectId } from '@apify/utilities';
import { captureOutput } from '@oclif/test';

import { LoginCommand } from '../../src/commands/login.js';
import { getLocalKeyValueStorePath } from '../../src/lib/utils.js';
import { waitForBuildToFinishWithTimeout } from '../__setup__/build-utils.js';
import { TEST_USER_TOKEN, testUserClient } from '../__setup__/config.js';
import { useAuthSetup } from '../__setup__/hooks/useAuthSetup.js';
import { useTempPath } from '../__setup__/hooks/useTempPath.js';

const ACTOR_NAME = `call-my-actor-${cryptoRandomObjectId(6)}-${process.version.split('.')[0]}-${platform()}`;
const EXPECTED_OUTPUT = {
	test: Math.random(),
};
const EXPECTED_INPUT = {
	myTestInput: Math.random(),
};
const EXPECTED_INPUT_CONTENT_TYPE = 'application/json';

const pathToInputJson = fileURLToPath(new URL('../__setup__/test-data/input-file.json', import.meta.url));
const expectedInputFile = JSON.parse(readFileSync(pathToInputJson, 'utf-8'));

useAuthSetup({ perTest: false });

const { beforeAllCalls, afterAllCalls, joinPath, toggleCwdBetweenFullAndParentPath, stdin } = useTempPath(ACTOR_NAME, {
	cwd: true,
	cwdParent: true,
	create: true,
	remove: true,
	withStdinMock: true,
});

const { CreateCommand } = await import('../../src/commands/create.js');
const { ActorsPushCommand } = await import('../../src/commands/actors/push.js');
const { ActorsCallCommand } = await import('../../src/commands/actors/call.js');

describe('apify call', () => {
	let actorId: string;
	let apifyId: string;

	beforeAll(async () => {
		await beforeAllCalls();

		const { username } = await testUserClient.user('me').get();

		await LoginCommand.run(['--token', TEST_USER_TOKEN], import.meta.url);
		await CreateCommand.run(
			[ACTOR_NAME, '--template', 'project_empty', '--skip-dependency-install'],
			import.meta.url,
		);

		const actCode = `
        import { Actor } from 'apify';

        Actor.main(async () => {
            await Actor.setValue('OUTPUT', ${JSON.stringify(EXPECTED_OUTPUT)});
            console.log('Done.');
        });
        `;
		writeFileSync(joinPath('src/main.js'), actCode, { flag: 'w' });

		const inputFile = joinPath(getLocalKeyValueStorePath(), 'INPUT.json');

		writeFileSync(inputFile, JSON.stringify(EXPECTED_INPUT), { flag: 'w' });

		toggleCwdBetweenFullAndParentPath();

		await ActorsPushCommand.run(['--no-prompt', '--force'], import.meta.url);

		actorId = `${username}/${ACTOR_NAME}`;

		// Build must finish before doing `apify call`, otherwise we would get nonexisting build with "LATEST" tag error.
		const builds = await testUserClient.actor(actorId).builds().list();
		const lastBuild = builds.items.pop();
		await waitForBuildToFinishWithTimeout(testUserClient, lastBuild!.id);

		apifyId = await testUserClient
			.actor(actorId)
			.get()
			.then((actor) => actor!.id);

		stdin.end();
	});

	afterAll(async () => {
		await testUserClient.actor(actorId).delete();
		await afterAllCalls();
	});

	it('without actId', async () => {
		await ActorsCallCommand.run([], import.meta.url);
		const actorClient = testUserClient.actor(actorId);
		const runs = await actorClient.runs().list();
		const lastRun = runs.items.pop();
		const lastRunDetail = await testUserClient.run(lastRun!.id).get();
		const output = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('OUTPUT');
		const input = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('INPUT');

		expect(EXPECTED_OUTPUT).toStrictEqual(output!.value);
		expect(EXPECTED_INPUT).toStrictEqual(input!.value);
		expect(EXPECTED_INPUT_CONTENT_TYPE).toStrictEqual(input!.contentType);
	});

	it('should work with just the Actor name', async () => {
		await expect(ActorsCallCommand.run([ACTOR_NAME], import.meta.url)).resolves.toBeUndefined();

		const actorClient = testUserClient.actor(actorId);
		const runs = await actorClient.runs().list();
		const lastRun = runs.items.pop();
		const lastRunDetail = await testUserClient.run(lastRun!.id).get();
		const output = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('OUTPUT');
		const input = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('INPUT');

		expect(EXPECTED_OUTPUT).toStrictEqual(output!.value);
		expect(EXPECTED_INPUT).toStrictEqual(input!.value);
		expect(EXPECTED_INPUT_CONTENT_TYPE).toStrictEqual(input!.contentType);
	});

	it('should work with just the Actor ID', async () => {
		await expect(ActorsCallCommand.run([apifyId], import.meta.url)).resolves.toBeUndefined();

		const actorClient = testUserClient.actor(actorId);
		const runs = await actorClient.runs().list();
		const lastRun = runs.items.pop();
		const lastRunDetail = await testUserClient.run(lastRun!.id).get();
		const output = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('OUTPUT');
		const input = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('INPUT');

		expect(EXPECTED_OUTPUT).toStrictEqual(output!.value);
		expect(EXPECTED_INPUT).toStrictEqual(input!.value);
		expect(EXPECTED_INPUT_CONTENT_TYPE).toStrictEqual(input!.contentType);
	});

	it('should work with passed in input', async () => {
		const expectedInput = {
			hello: 'from cli',
		};

		const string = JSON.stringify(expectedInput);

		await expect(ActorsCallCommand.run([ACTOR_NAME, '--input', string], import.meta.url)).resolves.toBeUndefined();

		const actorClient = testUserClient.actor(actorId);
		const runs = await actorClient.runs().list();
		const lastRun = runs.items.pop();
		const lastRunDetail = await testUserClient.run(lastRun!.id).get();
		const input = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('INPUT');

		expect(expectedInput).toStrictEqual(input!.value);
		expect(EXPECTED_INPUT_CONTENT_TYPE).toStrictEqual(input!.contentType);
	});

	it('should work with passed in input file', async () => {
		await expect(
			ActorsCallCommand.run([ACTOR_NAME, '--input-file', pathToInputJson], import.meta.url),
		).resolves.toBeUndefined();

		const actorClient = testUserClient.actor(actorId);
		const runs = await actorClient.runs().list();
		const lastRun = runs.items.pop();
		const lastRunDetail = await testUserClient.run(lastRun!.id).get();
		const input = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('INPUT');

		expect(expectedInputFile).toStrictEqual(input!.value);
		expect(EXPECTED_INPUT_CONTENT_TYPE).toStrictEqual(input!.contentType);
	});

	// TODO: move this to cucumber, much easier to test
	it.skip('should work with stdin input without --input or --input-file', async () => {
		const expectedInput = {
			hello: 'from cli',
		};

		const string = JSON.stringify(expectedInput);

		const { error } = await captureOutput(async () => {
			stdin.reset();
			setTimeout(() => {
				stdin.send(`${string}\n`);

				setTimeout(() => {
					stdin.end();
				}, 50);
			}, 1000);

			return ActorsCallCommand.run([ACTOR_NAME], import.meta.url);
		});

		expect(error).toBeUndefined();

		const actorClient = testUserClient.actor(actorId);
		const runs = await actorClient.runs().list();
		const lastRun = runs.items.pop();
		const lastRunDetail = await testUserClient.run(lastRun!.id).get();
		const input = await testUserClient.keyValueStore(lastRunDetail!.defaultKeyValueStoreId).getRecord('INPUT');

		expect(expectedInput).toStrictEqual(input!.value);
		expect(EXPECTED_INPUT_CONTENT_TYPE).toStrictEqual(input!.contentType);
	});
});


================================================
File: /test/commands/windows/create.test.ts
================================================
import { existsSync } from 'node:fs';

import { useTempPath } from '../../__setup__/hooks/useTempPath.js';

const actName = 'create-my-spaced-actor';
const { beforeAllCalls, afterAllCalls, joinPath } = useTempPath('spaced actor', {
	create: true,
	remove: true,
	cwd: true,
	cwdParent: false,
});

const { CreateCommand } = await import('../../../src/commands/create.js');

describe.runIf(process.env.FORCE_WINDOWS_TESTS || process.platform === 'win32')('apify create on windows', () => {
	beforeEach(async () => {
		await beforeAllCalls();
	});

	afterEach(async () => {
		await afterAllCalls();
	});

	it('works for creating an actor when the folder path contains spaces', async () => {
		const ACT_TEMPLATE = 'python-playwright';
		await CreateCommand.run([actName, '--template', ACT_TEMPLATE], import.meta.url);

		// check files structure
		expect(existsSync(joinPath(actName))).toBeTruthy();
	});
});


================================================
File: /test/commands/init.test.ts
================================================
import { existsSync } from 'node:fs';

import { KEY_VALUE_STORE_KEYS } from '@apify/consts';
import { loadJsonFileSync } from 'load-json-file';
import { writeJsonFile } from 'write-json-file';

import { EMPTY_LOCAL_CONFIG, LOCAL_CONFIG_PATH } from '../../src/lib/consts.js';
import { getLocalKeyValueStorePath } from '../../src/lib/utils.js';
import { useTempPath } from '../__setup__/hooks/useTempPath.js';

const actName = 'init-my-actor';
const { beforeAllCalls, afterAllCalls, joinPath } = useTempPath(actName, {
	create: true,
	remove: true,
	cwd: true,
	cwdParent: false,
});

const { InitCommand } = await import('../../src/commands/init.js');

describe('apify init', () => {
	beforeEach(async () => {
		await beforeAllCalls();
	});

	afterEach(async () => {
		await afterAllCalls();
	});

	it('correctly creates basic structure with empty INPUT.json', async () => {
		await InitCommand.run(['-y', actName], import.meta.url);

		// Check that it won't create deprecated config
		// TODO: We can remove this later
		const apifyJsonPath = 'apify.json';
		expect(existsSync(joinPath(apifyJsonPath))).toBeFalsy();

		expect(loadJsonFileSync(joinPath(LOCAL_CONFIG_PATH))).toStrictEqual(
			Object.assign(EMPTY_LOCAL_CONFIG, { name: actName }),
		);
		expect(
			loadJsonFileSync(joinPath(getLocalKeyValueStorePath(), `${KEY_VALUE_STORE_KEYS.INPUT}.json`)),
		).toStrictEqual({});
	});

	it('correctly creates structure with prefilled INPUT.json', async () => {
		const input = {
			title: 'Scrape data from a web page',
			type: 'object',
			schemaVersion: 1,
			properties: {
				url: {
					title: 'URL of the page',
					type: 'string',
					description: 'The URL of website you want to get the data from.',
					editor: 'textfield',
					prefill: 'https://www.apify.com/',
				},
			},
			required: ['url'],
		};
		const defaultActorJson = Object.assign(EMPTY_LOCAL_CONFIG, { name: actName, input });

		await writeJsonFile(joinPath('.actor/actor.json'), defaultActorJson);
		await InitCommand.run(['-y', actName], import.meta.url);

		// Check that it won't create deprecated config
		// TODO: We can remove this later
		const apifyJsonPath = 'apify.json';
		expect(existsSync(joinPath(apifyJsonPath))).toBeFalsy();
		expect(loadJsonFileSync(joinPath(LOCAL_CONFIG_PATH))).toStrictEqual(defaultActorJson);
		expect(
			loadJsonFileSync(joinPath(getLocalKeyValueStorePath(), `${KEY_VALUE_STORE_KEYS.INPUT}.json`)),
		).toStrictEqual({ url: 'https://www.apify.com/' });
	});
});


================================================
File: /test/commands/secrets/rm.test.ts
================================================
import { runCommand } from '@oclif/test';

import { SecretsAddCommand } from '../../../src/commands/secrets/add.js';
import { getSecretsFile } from '../../../src/lib/secrets.js';
import { useAuthSetup } from '../../__setup__/hooks/useAuthSetup.js';

const SECRET_KEY = 'mySecret';

useAuthSetup({ perTest: false });

describe('apify secrets:rm', () => {
	beforeAll(async () => {
		const secrets = getSecretsFile();
		if (!secrets[SECRET_KEY]) {
			await SecretsAddCommand.run([SECRET_KEY, 'owo'], import.meta.url);
		}
	});

	it('should work', async () => {
		const { error } = await runCommand(['secrets:rm', SECRET_KEY], import.meta.url);

		expect(error).toBeFalsy();

		const secrets = getSecretsFile();
		expect(secrets[SECRET_KEY]).to.eql(undefined);
	});
});


================================================
File: /test/commands/secrets/add.test.ts
================================================
import { runCommand } from '@oclif/test';

import { SecretRmCommand } from '../../../src/commands/secrets/rm.js';
import { getSecretsFile } from '../../../src/lib/secrets.js';
import { useAuthSetup } from '../../__setup__/hooks/useAuthSetup.js';

const SECRET_KEY = 'mySecret';
const SECRET_KEY_2 = 'mySecret2';
const SECRET_VALUE = 'mySecretValue';

useAuthSetup({ perTest: false });

describe('apify secrets:add', () => {
	beforeAll(async () => {
		const secrets = getSecretsFile();
		if (secrets[SECRET_KEY]) {
			await SecretRmCommand.run([SECRET_KEY], import.meta.url);
		}
	});

	it('should work', async () => {
		const { error } = await runCommand(['secrets:add', SECRET_KEY, SECRET_VALUE], import.meta.url);

		expect(error).toBeFalsy();

		const secrets = getSecretsFile();
		expect(secrets[SECRET_KEY]).to.eql(SECRET_VALUE);
	});

	it('should work with alias', async () => {
		const { error } = await runCommand(['secrets add', SECRET_KEY_2, SECRET_VALUE], import.meta.url);

		expect(error).toBeFalsy();

		const secrets = getSecretsFile();
		expect(secrets[SECRET_KEY_2]).to.eql(SECRET_VALUE);
	});

	afterAll(async () => {
		const secrets = getSecretsFile();

		if (secrets[SECRET_KEY]) {
			await SecretRmCommand.run([SECRET_KEY], import.meta.url);
		}

		if (secrets[SECRET_KEY_2]) {
			await SecretRmCommand.run([SECRET_KEY_2], import.meta.url);
		}
	});
});


================================================
File: /test/commands/push.test.ts
================================================
/* eslint-disable @typescript-eslint/no-explicit-any */
import { existsSync, unlinkSync, writeFileSync } from 'node:fs';
import { mkdir, writeFile } from 'node:fs/promises';
import { platform } from 'node:os';

import { ACTOR_SOURCE_TYPES, SOURCE_FILE_FORMATS } from '@apify/consts';
import { cryptoRandomObjectId } from '@apify/utilities';
import type { ActorCollectionCreateOptions } from 'apify-client';
import { loadJsonFileSync } from 'load-json-file';
import { writeJsonFileSync } from 'write-json-file';

import { LOCAL_CONFIG_PATH } from '../../src/lib/consts.js';
import { createSourceFiles, getActorLocalFilePaths, getLocalUserInfo } from '../../src/lib/utils.js';
import { TEST_USER_TOKEN, testUserClient } from '../__setup__/config.js';
import { useAuthSetup } from '../__setup__/hooks/useAuthSetup.js';
import { useConsoleSpy } from '../__setup__/hooks/useConsoleSpy.js';
import { useTempPath } from '../__setup__/hooks/useTempPath.js';

const ACTOR_NAME = `push-cli-test-${cryptoRandomObjectId(6)}`;
const TEST_ACTOR: ActorCollectionCreateOptions = {
	// Less likely to encounter a name conflict when multiple node versions are running tests
	name: `push-my-cli-test-${cryptoRandomObjectId(6)}-${process.version.split('.')[0]}-${platform()}`,
	isPublic: false,
	versions: [
		{
			versionNumber: '0.0',
			sourceType: 'SOURCE_FILES' as never,
			buildTag: 'latest',
			sourceFiles: [],
		},
	],
};
const ACT_TEMPLATE = 'project_empty';

useAuthSetup({ perTest: false });

const {
	beforeAllCalls,
	afterAllCalls,
	joinPath,
	tmpPath,
	toggleCwdBetweenFullAndParentPath,
	joinCwdPath,
	forceNewCwd,
} = useTempPath(ACTOR_NAME, { create: true, remove: true, cwd: true, cwdParent: true });

const { LoginCommand } = await import('../../src/commands/login.js');
const { CreateCommand } = await import('../../src/commands/create.js');
const { ActorsPushCommand } = await import('../../src/commands/actors/push.js');

describe('apify push', () => {
	const actorsForCleanup = new Set<string>();

	const consoleSpy = useConsoleSpy();

	beforeAll(async () => {
		await beforeAllCalls();

		await LoginCommand.run(['--token', TEST_USER_TOKEN], import.meta.url);
		await CreateCommand.run([ACTOR_NAME, '--template', ACT_TEMPLATE, '--skip-dependency-install'], import.meta.url);

		toggleCwdBetweenFullAndParentPath();
	});

	afterAll(async () => {
		await afterAllCalls();

		for (const actorId of actorsForCleanup) {
			const actorClient = testUserClient.actor(actorId);
			await actorClient.delete();
		}
	});

	it('should work without actorId', async () => {
		const actorJson = loadJsonFileSync<{
			environmentVariables: Record<string, string>;
			name: string;
			version: string;
		}>(joinPath(LOCAL_CONFIG_PATH));
		actorJson.environmentVariables = {
			MY_ENV_VAR: 'envVarValue',
		};
		writeJsonFileSync(joinPath(LOCAL_CONFIG_PATH), actorJson);

		await ActorsPushCommand.run(['--no-prompt', '--force'], import.meta.url);

		const userInfo = await getLocalUserInfo();
		const { name } = actorJson;
		const actorId = `${userInfo.username}/${name}`;
		actorsForCleanup.add(actorId);
		const createdActorClient = testUserClient.actor(actorId);
		const createdActor = await createdActorClient.get();
		const createdActorVersion = await createdActorClient.version(actorJson.version).get();

		const filePathsToPush = await getActorLocalFilePaths(tmpPath);
		const sourceFiles = await createSourceFiles(filePathsToPush, tmpPath);

		if (createdActor) await createdActorClient.delete();

		expect(createdActorVersion!.versionNumber).to.be.eql(actorJson.version);
		expect(createdActorVersion!.buildTag).to.be.eql('latest');
		expect(createdActorVersion!.envVars).to.be.eql([
			{
				name: 'MY_ENV_VAR',
				value: 'envVarValue',
			},
		]);
		// TODO: vlad, fix this too
		expect((createdActorVersion as any)!.sourceFiles.sort()).to.be.eql(sourceFiles.sort());
		expect(createdActorVersion!.sourceType).to.be.eql(ACTOR_SOURCE_TYPES.SOURCE_FILES);
	});

	it('should work with actorId', async () => {
		let testActor = await testUserClient.actors().create(TEST_ACTOR);
		const testActorClient = testUserClient.actor(testActor.id);
		const actorJson = loadJsonFileSync<{ version: string }>(joinPath(LOCAL_CONFIG_PATH));

		await ActorsPushCommand.run(['--no-prompt', '--force', testActor.id], import.meta.url);

		actorsForCleanup.add(testActor.id);

		testActor = (await testActorClient.get())!;
		const testActorVersion = await testActorClient.version(actorJson!.version).get();

		const filePathsToPush = await getActorLocalFilePaths(tmpPath);
		const sourceFiles = await createSourceFiles(filePathsToPush, tmpPath);

		if (testActor) await testActorClient.delete();

		expect(testActorVersion!.versionNumber).to.be.eql(actorJson.version);
		expect(testActorVersion!.buildTag).to.be.eql('latest');
		expect(testActorVersion!.envVars).to.be.eql([
			{
				name: 'MY_ENV_VAR',
				value: 'envVarValue',
			},
		]);
		expect((testActorVersion as any).sourceFiles.sort()).to.be.eql(sourceFiles.sort());
		expect(testActorVersion!.sourceType).to.be.eql(ACTOR_SOURCE_TYPES.SOURCE_FILES);
	});

	it('should not rewrite current Actor envVars', async () => {
		const testActorWithEnvVars = { ...TEST_ACTOR };
		testActorWithEnvVars.versions = [
			{
				versionNumber: '0.0',
				sourceType: 'SOURCE_FILES' as never,
				buildTag: 'latest',
				sourceFiles: [],
				envVars: [
					{
						name: 'MY_TEST',
						value: 'myValue',
					},
				],
			},
		];
		let testActor = await testUserClient.actors().create(testActorWithEnvVars);
		actorsForCleanup.add(testActor.id);
		const testActorClient = testUserClient.actor(testActor.id);

		const actorJson = loadJsonFileSync<{ environmentVariables?: Record<string, string>; version: string }>(
			joinPath(LOCAL_CONFIG_PATH),
		);
		delete actorJson.environmentVariables;
		writeJsonFileSync(joinPath(LOCAL_CONFIG_PATH), actorJson);

		await ActorsPushCommand.run(['--no-prompt', testActor.id], import.meta.url);

		testActor = (await testActorClient.get())!;
		const testActorVersion = await testActorClient.version(actorJson.version).get();

		const filePathsToPush = await getActorLocalFilePaths(tmpPath);
		const sourceFiles = await createSourceFiles(filePathsToPush, tmpPath);

		if (testActor) await testActorClient.delete();

		expect(testActorVersion!.versionNumber).to.be.eql(actorJson.version);
		expect(testActorVersion!.envVars).to.be.eql(testActorWithEnvVars.versions[0].envVars);
		expect((testActorVersion as any).sourceFiles.sort()).to.be.eql(sourceFiles.sort());
		expect(testActorVersion!.sourceType).to.be.eql(ACTOR_SOURCE_TYPES.SOURCE_FILES);
	});

	it('should upload zip for source files larger that 3MB', async () => {
		const testActorWithEnvVars = { ...TEST_ACTOR };
		testActorWithEnvVars.versions = [
			{
				versionNumber: '0.0',
				sourceType: 'TARBALL' as any,
				buildTag: 'latest',
				tarballUrl: 'http://example.com/my_test.zip',
				envVars: [
					{
						name: 'MY_TEST',
						value: 'myValue',
					},
				],
			},
		];
		let testActor = await testUserClient.actors().create(testActorWithEnvVars);
		actorsForCleanup.add(testActor.id);
		const testActorClient = testUserClient.actor(testActor.id);
		const actorJson = loadJsonFileSync<{ environmentVariables?: Record<string, string>; version: string }>(
			joinPath(LOCAL_CONFIG_PATH),
		);

		delete actorJson.environmentVariables;
		writeJsonFileSync(joinPath(LOCAL_CONFIG_PATH), actorJson);

		// Create large file to ensure Actor will be uploaded as zip
		writeFileSync(joinPath('3mb-file.txt'), Buffer.alloc(1024 * 1024 * 3));

		await ActorsPushCommand.run(['--no-prompt', testActor.id], import.meta.url);

		// Remove the big file so sources in following tests are not zipped
		unlinkSync(joinPath('3mb-file.txt'));

		testActor = (await testActorClient.get())!;
		const testActorVersion = await testActorClient.version(actorJson.version).get();
		const store = await testUserClient.keyValueStores().getOrCreate(`actor-${testActor.id}-source`);
		await testUserClient.keyValueStore(store.id).delete(); // We just needed the store ID, we can clean up now

		if (testActor) await testActorClient.delete();

		expect(testActorVersion).to.be.eql({
			versionNumber: actorJson.version,
			buildTag: 'latest',
			tarballUrl:
				`${testActorClient.baseUrl}/key-value-stores/${store.id}` +
				`/records/version-${actorJson.version}.zip?disableRedirect=true`,
			envVars: testActorWithEnvVars.versions[0].envVars,
			sourceType: ACTOR_SOURCE_TYPES.TARBALL,
		});
	});

	it('typescript files should be treated as text', async () => {
		const { name, version } = loadJsonFileSync<{
			environmentVariables?: Record<string, string>;
			version: string;
			name: string;
		}>(joinPath(LOCAL_CONFIG_PATH));

		writeFileSync(joinPath('some-typescript-file.ts'), `console.log('ok');`);

		await ActorsPushCommand.run(['--no-prompt', '--force'], import.meta.url);

		if (existsSync(joinPath('some-typescript-file.ts'))) unlinkSync(joinPath('some-typescript-file.ts'));

		const userInfo = await getLocalUserInfo();
		const actorId = `${userInfo.username}/${name}`;
		actorsForCleanup.add(actorId);
		const createdActorClient = testUserClient.actor(actorId);
		const createdActor = await createdActorClient.get();
		const createdActorVersion = await createdActorClient.version(version).get();

		if (createdActor) await createdActorClient.delete();

		expect(
			(createdActorVersion as any).sourceFiles.find((file: any) => file.name === 'some-typescript-file.ts')
				.format,
		).to.be.equal(SOURCE_FILE_FORMATS.TEXT);
	});

	it('should not push Actor when there is newer version on platform', async () => {
		const testActor = await testUserClient.actors().create(TEST_ACTOR);
		actorsForCleanup.add(testActor.id);
		const testActorClient = testUserClient.actor(testActor.id);
		const actorJson = loadJsonFileSync<{ version: string }>(joinPath(LOCAL_CONFIG_PATH));

		// @ts-expect-error Wrong typing of update method
		await testActorClient.version(actorJson.version).update({ buildTag: 'beta' });

		try {
			await ActorsPushCommand.run(['--no-prompt', testActor.id], import.meta.url);
		} catch (e) {
			expect((e as Error).message).to.includes('is already on the platform');
		}
	});

	it('should not push Actor when there are no files to push', async () => {
		toggleCwdBetweenFullAndParentPath();

		await mkdir(joinCwdPath('empty-dir'), { recursive: true });

		forceNewCwd('empty-dir');

		await ActorsPushCommand.run(['--no-prompt'], import.meta.url);

		expect(consoleSpy.errorSpy).toHaveBeenCalled();

		const lastCall = consoleSpy.errorSpy.mock.calls.at(-1)!;
		expect(lastCall[1]).to.include('You need to call this command from a folder that has an Actor in it');
	});

	it('should not push when the folder does not seem to have a valid Actor', async () => {
		toggleCwdBetweenFullAndParentPath();

		await mkdir(joinCwdPath('not-an-actor-i-promise'), { recursive: true });

		forceNewCwd('not-an-actor-i-promise');

		await writeFile(joinCwdPath('owo.txt'), 'Lorem ipsum');

		await ActorsPushCommand.run(['--no-prompt'], import.meta.url);

		expect(consoleSpy.errorSpy).toHaveBeenCalled();

		const lastCall = consoleSpy.errorSpy.mock.calls.at(-1)!;
		expect(lastCall[1]).to.include('A valid Actor could not be found in the current directory.');
	});
});


================================================
File: /test/commands/pull.test.ts
================================================
/* eslint-disable @typescript-eslint/no-explicit-any */
import { existsSync } from 'node:fs';
import { rm } from 'node:fs/promises';
import { join } from 'node:path';

import { runCommand } from '@oclif/test';
import type { ActorCollectionCreateOptions } from 'apify-client';
import { loadJsonFileSync } from 'load-json-file';
import { writeJsonFile } from 'write-json-file';

import { LoginCommand } from '../../src/commands/login.js';
import { DEPRECATED_LOCAL_CONFIG_NAME, LOCAL_CONFIG_PATH } from '../../src/lib/consts.js';
import { TEST_USER_TOKEN, testUserClient } from '../__setup__/config.js';
import { useAuthSetup } from '../__setup__/hooks/useAuthSetup.js';
import { useProcessMock } from '../__setup__/hooks/useProcessMock.js';

const TEST_ACTOR_SOURCE_FILES: ActorCollectionCreateOptions = {
	isPublic: false,
	versions: [
		{
			versionNumber: '0.0',
			// TODO: vlad, export these enums
			sourceType: 'SOURCE_FILES' as never,
			buildTag: 'latest',
			sourceFiles: [
				{
					name: '.actor',
					// TODO: what? is this not typed correctly?
					folder: true,
				} as never,
				{
					name: '.actor/Dockerfile',
					format: 'TEXT',
					content:
						'# First, specify the base Docker image.\n# You can see the Docker images from Apify at https://hub.docker.com/r/apify/.\n# You can also use any other image from Docker Hub.\nFROM apify/actor-python:3.11\n\n# Second, copy just requirements.txt into the Actor image,\n# since it should be the only file that affects the dependency install in the next step,\n# in order to speed up the build\nCOPY requirements.txt ./\n\n# Install the packages specified in requirements.txt,\n# Print the installed Python version, pip version\n# and all installed packages with their versions for debugging\nRUN echo "Python version:" \\\n && python --version \\\n && echo "Pip version:" \\\n && pip --version \\\n && echo "Installing dependencies:" \\\n && pip install -r requirements.txt \\\n && echo "All installed Python packages:" \\\n && pip freeze\n\n# Next, copy the remaining files and directories with the source code.\n# Since we do this after installing the dependencies, quick build will be really fast\n# for most source file changes.\nCOPY . ./\n\n# Specify how to launch the source code of your Actor.\n# By default, the "python3 -m src" command is run\nCMD ["python3", "-m", "src"]\n',
				},
				{
					name: '.actor/actor.json',
					format: 'TEXT',
					content:
						'{"actorSpecification": 1,"name": "","title": "Getting Started with Apify Python SDK","description": "Adds two integers.",' +
						'"version": "0.0","meta": {"templateId": "python-start"},"dockerfile": "./Dockerfile",' +
						'"storages": {"dataset": {"actorSpecification": 1,"title": "Numbers and their sums",' +
						'"views": {"sums": {"title": "A sum of two numbers",' +
						'"transformation": {"fields": ["sum","first_number","second_number"]},' +
						'"display": {"component": "table","properties": {"sum": {"label": "Sum","format": "number"},' +
						'"first_number": {"label": "First number","format": "number"},' +
						'"second_number": {"label": "Second number","format": "number"}}}}}}}}',
				},
				{
					name: 'src',
					folder: true,
				} as never,
				{
					name: 'src/__init__.py',
					format: 'TEXT',
					content: '',
				},
				{
					name: 'README.md',
					format: 'TEXT',
					content:
						'# Start with Python template\n\nA simple Python example of core Actor and Apify SDK features. It reads and validates user input with schema, computes a result and saves it to storage.\n\n## Getting Started\n\n### Install Apify CLI\n\n#### Using Homebrew\n\n```Bash\nbrew install apify-cli\n```\n\n#### Using NPM\n\n```Bash\nnpm -g install apify-cli\n```\n\n### Create a new Actor using this template\n\n```Bash\napify create my-python-actor -t python-start\n```\n\n### Run the Actor locally\n\n```Bash\ncd my-python-actor\napify run\n```\n\n## Deploy on Apify\n\n### Log in to Apify\n\nYou will need to provide your [Apify API Token](https://console.apify.com/settings/integrations) to complete this action.\n\n```Bash\napify login\n```\n\n### Deploy your Actor\n\nThis command will deploy and build the Actor on the Apify Platform. You can find your newly created Actor under [Actors -> My Actors](https://console.apify.com/actors?tab=my).\n\n```Bash\napify push\n```\n\n## Documentation reference\n\nTo learn more about Apify and Actors, take a look at the following resources:\n\n- [Apify SDK for Python documentation](https://docs.apify.com/sdk/python)\n- [Apify Platform documentation](https://docs.apify.com/platform)\n- [Join our developer community on Discord](https://discord.com/invite/jyEM2PRvMU)\n',
				},
				{
					name: 'requirements.txt',
					format: 'TEXT',
					content:
						'# Add your dependencies here.\n# See https://pip.pypa.io/en/latest/reference/requirements-file-format/\n# for how to format them\napify ~= 1.0.0\n',
				},
			],
		},
	],
};

const TEST_ACTOR_GITHUB_GIST: ActorCollectionCreateOptions = {
	isPublic: false,
	versions: [
		{
			versionNumber: '0.0',
			sourceType: 'GITHUB_GIST' as never,
			buildTag: 'latest',
			gitHubGistUrl: 'https://gist.github.com/DennisKallerhoff/32f1efd686e11f6a05f1af87bddb1f1a',
		},
	],
};

const TEST_ACTOR_GIT_REPO: ActorCollectionCreateOptions = {
	isPublic: false,
	versions: [
		{
			versionNumber: '0.0',
			sourceType: 'GIT_REPO' as never,
			buildTag: 'latest',
			gitRepoUrl: 'https://github.com/HonzaTuron/baidu-scraper#multipage',
		},
	],
};

useAuthSetup({ perTest: false });

let cwd: string = process.cwd();

function setProcessCwd(newCwd: string) {
	cwd = newCwd;
}

useProcessMock({ cwdMock: () => cwd });

const { ActorsPullCommand } = await import('../../src/commands/actors/pull.js');

describe('apify pull', () => {
	const actorsForCleanup = new Set<string>();
	const actorNamesForCleanup = new Set<string>();

	beforeAll(async () => {
		await LoginCommand.run(['--token', TEST_USER_TOKEN], import.meta.url);
	});

	afterAll(async () => {
		for (const id of actorsForCleanup) {
			await testUserClient.actor(id).delete();
		}

		for (const name of actorNamesForCleanup) {
			await rm(name, { recursive: true, force: true });
		}
	});

	it('should fail outside Actor folder without actorId defined', async () => {
		const { error } = await runCommand(['pull'], import.meta.url);

		expect(error).toBeTruthy();
		expect(error?.message).toEqual('Cannot find Actor in this directory.');
	});

	it('should work with Actor SOURCE_FILES', async () => {
		const testActor = await testUserClient
			.actors()
			.create({ name: `pull-test-${Date.now()}`, ...TEST_ACTOR_SOURCE_FILES });
		actorsForCleanup.add(testActor.id);
		actorNamesForCleanup.add(testActor.name);

		const testActorClient = testUserClient.actor(testActor.id);
		const actorFromServer = await testActorClient.get();

		await ActorsPullCommand.run([testActor.id], import.meta.url);

		const actorJson = loadJsonFileSync<{ name: string }>(join(testActor.name, LOCAL_CONFIG_PATH));

		expect(actorJson.name).to.be.eql(actorFromServer!.name);
	});

	it('should work with GITHUB_GIST', async () => {
		const testActor = await testUserClient
			.actors()
			.create({ name: `pull-test-${Date.now()}`, ...TEST_ACTOR_GITHUB_GIST });
		actorsForCleanup.add(testActor.id);
		actorNamesForCleanup.add(testActor.name);

		await ActorsPullCommand.run([testActor.id], import.meta.url);

		const actorPackageJson = loadJsonFileSync<{ name: string }>(join(testActor.name, 'package.json'));

		expect(actorPackageJson.name).to.be.eql('act-in-gist');
	});

	it('should work with GIT_REPO', async () => {
		const testActor = await testUserClient
			.actors()
			.create({ name: `pull-test-${Date.now()}`, ...TEST_ACTOR_GIT_REPO });
		actorsForCleanup.add(testActor.id);
		actorNamesForCleanup.add(testActor.name);

		await ActorsPullCommand.run([testActor.id], import.meta.url);

		const actorJson = loadJsonFileSync<{ name: string }>(join(testActor.name, DEPRECATED_LOCAL_CONFIG_NAME));

		expect(actorJson.name).to.be.eql('baidu-scraper');
	});

	it('should work without actor name', async () => {
		const testActor = await testUserClient
			.actors()
			.create({ name: `pull-test-${Date.now()}`, ...TEST_ACTOR_SOURCE_FILES });
		actorsForCleanup.add(testActor.id);
		actorNamesForCleanup.add('pull-test-no-name');

		const contentBeforeEdit = JSON.parse((TEST_ACTOR_SOURCE_FILES.versions![0] as any).sourceFiles[2].content);
		contentBeforeEdit.name = testActor.name;
		(TEST_ACTOR_SOURCE_FILES.versions![0] as any).sourceFiles[2].content = contentBeforeEdit;

		await writeJsonFile(
			join('pull-test-no-name', LOCAL_CONFIG_PATH),
			(TEST_ACTOR_SOURCE_FILES.versions![0] as any).sourceFiles[2].content,
		);

		setProcessCwd(join(cwd, 'pull-test-no-name'));
		await ActorsPullCommand.run([], import.meta.url);

		expect(existsSync(join('pull-test-no-name', 'src/__init__.py'))).to.be.eql(true);
	});
});


================================================
File: /test/commands/log_in_out.test.ts
================================================
import { existsSync } from 'node:fs';

import axios from 'axios';
import { loadJsonFileSync } from 'load-json-file';
import _ from 'underscore';

import { AUTH_FILE_PATH } from '../../src/lib/consts.js';
import { TEST_USER_BAD_TOKEN, TEST_USER_TOKEN, testUserClient } from '../__setup__/config.js';
import { useAuthSetup } from '../__setup__/hooks/useAuthSetup.js';

vitest.setConfig({ restoreMocks: false });
useAuthSetup();

vitest.mock('open', () => ({
	default: (url: string) => console.error(`Open URL: ${url}`),
}));

const { LoginCommand } = await import('../../src/commands/login.js');
const { LogoutCommand } = await import('../../src/commands/logout.js');

describe('apify login and logout', () => {
	let spy: import('vitest').MockInstance<Parameters<(typeof console)['error']>, void>;

	beforeEach(() => {
		spy = vitest.spyOn(console, 'error');
	});

	it('should end with Error with bad token', async () => {
		await LoginCommand.run(['--token', TEST_USER_BAD_TOKEN], import.meta.url);

		expect(spy).toHaveBeenCalledTimes(1);
		expect(spy.mock.calls[0][0]).to.include('Error:');
	});

	it('should work with correct token', async () => {
		await LoginCommand.run(['--token', TEST_USER_TOKEN], import.meta.url);

		const expectedUserInfo = Object.assign(await testUserClient.user('me').get(), { token: TEST_USER_TOKEN });
		const userInfoFromConfig = loadJsonFileSync(AUTH_FILE_PATH());

		expect(spy).toHaveBeenCalledTimes(1);
		expect(spy.mock.calls[0][0]).to.include('Success:');
		// Omit currentBillingPeriod, It can change during tests
		const floatFields = ['currentBillingPeriod', 'plan', 'createdAt'];
		expect(_.omit(expectedUserInfo, floatFields)).to.eql(_.omit(userInfoFromConfig, floatFields));

		await LogoutCommand.run([], import.meta.url);
		const isGlobalConfig = existsSync(AUTH_FILE_PATH());

		expect(isGlobalConfig).to.be.eql(false);
	});

	it('have correctly setup server for interactive login', async () => {
		await LoginCommand.run(['-m', 'console'], import.meta.url);

		const consoleInfo = spy.mock.calls[0][1];
		const consoleUrl = /"(http[s]?:\/\/[^"]*)"/.exec(consoleInfo)?.[1];

		const consoleUrlParams = new URL(consoleUrl!).searchParams;

		const localCliPort = consoleUrlParams.get('localCliPort');
		const localCliToken = consoleUrlParams.get('localCliToken');

		const response = await axios.post(
			`http://localhost:${localCliPort}/api/v1/login-token?token=${localCliToken}`,
			{ apiToken: TEST_USER_TOKEN },
			{ headers: { 'Content-Type': 'application/json' } },
		);

		expect(response.status).to.be.eql(200);

		const expectedUserInfo = Object.assign(await testUserClient.user('me').get(), { token: TEST_USER_TOKEN });
		const userInfoFromConfig = loadJsonFileSync(AUTH_FILE_PATH());

		expect(spy.mock.calls[2][0]).to.include('Success:');
		// Omit currentBillingPeriod, It can change during tests
		const floatFields = ['currentBillingPeriod', 'plan', 'createdAt'];
		expect(_.omit(expectedUserInfo, floatFields)).to.eql(_.omit(userInfoFromConfig, floatFields));
	});
});


================================================
File: /test/commands/run.test.ts
================================================
import { copyFileSync, existsSync, readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

import { APIFY_ENV_VARS } from '@apify/consts';
import { captureOutput } from '@oclif/test';
import { loadJsonFileSync } from 'load-json-file';
import { writeJsonFileSync } from 'write-json-file';

import { AUTH_FILE_PATH, EMPTY_LOCAL_CONFIG, LOCAL_CONFIG_PATH } from '../../src/lib/consts.js';
import { rimrafPromised } from '../../src/lib/files.js';
import {
	getLocalDatasetPath,
	getLocalKeyValueStorePath,
	getLocalRequestQueuePath,
	getLocalStorageDir,
} from '../../src/lib/utils.js';
import { TEST_USER_TOKEN } from '../__setup__/config.js';
import { useAuthSetup } from '../__setup__/hooks/useAuthSetup.js';
import { useTempPath } from '../__setup__/hooks/useTempPath.js';

const actName = 'run-my-actor';
const pathToDefaultsInputSchema = fileURLToPath(new URL('../__setup__/input-schemas/defaults.json', import.meta.url));
const pathToMissingRequiredInputSchema = fileURLToPath(
	new URL('../__setup__/input-schemas/missing-required-property.json', import.meta.url),
);
const pathToPrefillsInputSchema = fileURLToPath(new URL('../__setup__/input-schemas/prefills.json', import.meta.url));

const INPUT_SCHEMA_ACTOR_SRC = `
import { Actor } from 'apify';

Actor.main(async () => {
    const input = await Actor.getInput();

    await Actor.setValue('OUTPUT', input);

    console.log('Done.');
});
`;

useAuthSetup({ perTest: true });

const { beforeAllCalls, afterAllCalls, joinPath, toggleCwdBetweenFullAndParentPath } = useTempPath(actName, {
	create: true,
	remove: true,
	cwd: true,
	cwdParent: true,
});

const { CreateCommand } = await import('../../src/commands/create.js');
const { RunCommand } = await import('../../src/commands/run.js');
const { LoginCommand } = await import('../../src/commands/login.js');

describe('apify run', () => {
	beforeAll(async () => {
		await beforeAllCalls();

		await CreateCommand.run([actName, '--template', 'project_empty'], import.meta.url);
		toggleCwdBetweenFullAndParentPath();
	});

	afterAll(async () => {
		await afterAllCalls();
	});

	it('run act with output', async () => {
		const expectOutput = {
			my: 'output',
		};
		const actCode = `
        import { Actor } from 'apify';

        Actor.main(async () => {
            const input = await Actor.getInput();

            const output = ${JSON.stringify(expectOutput)};
            await Actor.setValue('OUTPUT', output);
            console.log('Done.');
        });
        `;
		writeFileSync(joinPath('src/main.js'), actCode, { flag: 'w' });

		await RunCommand.run([], import.meta.url);

		// check act output
		const actOutputPath = joinPath(getLocalKeyValueStorePath(), 'OUTPUT.json');
		const actOutput = loadJsonFileSync(actOutputPath);
		expect(actOutput).toStrictEqual(expectOutput);
	});

	it(`run with env vars from "${LOCAL_CONFIG_PATH}"`, async () => {
		const testEnvVars = {
			TEST_LOCAL: 'testValue',
		};

		await LoginCommand.run(['--token', TEST_USER_TOKEN], import.meta.url);

		const actCode = `
        import { Actor } from 'apify';

        Actor.main(async () => {
            await Actor.setValue('OUTPUT', process.env);
            console.log('Done.');
        });
        `;
		writeFileSync(joinPath('src/main.js'), actCode, { flag: 'w' });

		const apifyJson = EMPTY_LOCAL_CONFIG;
		apifyJson.environmentVariables = testEnvVars;
		writeJsonFileSync(joinPath(LOCAL_CONFIG_PATH), apifyJson);

		await RunCommand.run([], import.meta.url);

		const actOutputPath = joinPath(getLocalKeyValueStorePath(), 'OUTPUT.json');

		const localEnvVars =
			loadJsonFileSync<Record<(typeof APIFY_ENV_VARS)[keyof typeof APIFY_ENV_VARS] | 'TEST_LOCAL', string>>(
				actOutputPath,
			);
		const auth = loadJsonFileSync<{ proxy: { password: string }; id: string; token: string }>(AUTH_FILE_PATH());

		expect(localEnvVars[APIFY_ENV_VARS.PROXY_PASSWORD]).toStrictEqual(auth.proxy.password);
		expect(localEnvVars[APIFY_ENV_VARS.USER_ID]).toStrictEqual(auth.id);
		expect(localEnvVars[APIFY_ENV_VARS.TOKEN]).toStrictEqual(auth.token);
		expect(localEnvVars.TEST_LOCAL).toStrictEqual(testEnvVars.TEST_LOCAL);
	});

	it(`run with env vars from "${LOCAL_CONFIG_PATH}" and custom script`, async () => {
		const testEnvVars = {
			TEST_LOCAL: 'testValue',
		};

		await LoginCommand.run(['--token', TEST_USER_TOKEN], import.meta.url);

		const actCode = `
        import { Actor } from 'apify';

        Actor.main(async () => {
            await Actor.setValue('OUTPUT', process.env);
            await Actor.setValue('owo', 'uwu');
            console.log('Done.');
        });
        `;

		writeFileSync(joinPath('src/other.js'), actCode, { flag: 'w' });

		const apifyJson = EMPTY_LOCAL_CONFIG;
		apifyJson.environmentVariables = testEnvVars;
		writeJsonFileSync(joinPath(LOCAL_CONFIG_PATH), apifyJson);

		const pkgJson = readFileSync(joinPath('package.json'), 'utf8');
		const parsedPkgJson = JSON.parse(pkgJson);
		parsedPkgJson.scripts.other = 'node src/other.js';
		writeFileSync(joinPath('package.json'), JSON.stringify(parsedPkgJson, null, 2), { flag: 'w' });

		await RunCommand.run(['--entrypoint', 'other'], import.meta.url);

		const actOutputPath = joinPath(getLocalKeyValueStorePath(), 'OUTPUT.json');

		const localEnvVars =
			loadJsonFileSync<Record<(typeof APIFY_ENV_VARS)[keyof typeof APIFY_ENV_VARS] | 'TEST_LOCAL', string>>(
				actOutputPath,
			);
		const auth = loadJsonFileSync<{ proxy: { password: string }; id: string; token: string }>(AUTH_FILE_PATH());

		expect(localEnvVars[APIFY_ENV_VARS.PROXY_PASSWORD]).toStrictEqual(auth.proxy.password);
		expect(localEnvVars[APIFY_ENV_VARS.USER_ID]).toStrictEqual(auth.id);
		expect(localEnvVars[APIFY_ENV_VARS.TOKEN]).toStrictEqual(auth.token);
		expect(localEnvVars.TEST_LOCAL).toStrictEqual(testEnvVars.TEST_LOCAL);

		const actOutputPath2 = joinPath(getLocalKeyValueStorePath(), 'owo.json');
		const actOutput2 = loadJsonFileSync(actOutputPath2);
		expect(actOutput2).toStrictEqual('uwu');
	});

	it(`run with env vars from "${LOCAL_CONFIG_PATH}" and direct path to script`, async () => {
		const testEnvVars = {
			TEST_LOCAL: 'testValue',
		};

		await LoginCommand.run(['--token', TEST_USER_TOKEN], import.meta.url);

		const actCode = `
        import { Actor } from 'apify';

        Actor.main(async () => {
            await Actor.setValue('OUTPUT', process.env);
            await Actor.setValue('two', 'can play');
            console.log('Done.');
        });
        `;

		writeFileSync(joinPath('src/other.js'), actCode, { flag: 'w' });

		const apifyJson = EMPTY_LOCAL_CONFIG;
		apifyJson.environmentVariables = testEnvVars;
		writeJsonFileSync(joinPath(LOCAL_CONFIG_PATH), apifyJson);

		await RunCommand.run(['--entrypoint', 'src/other.js'], import.meta.url);

		const actOutputPath = joinPath(getLocalKeyValueStorePath(), 'OUTPUT.json');

		const localEnvVars =
			loadJsonFileSync<Record<(typeof APIFY_ENV_VARS)[keyof typeof APIFY_ENV_VARS] | 'TEST_LOCAL', string>>(
				actOutputPath,
			);
		const auth = loadJsonFileSync<{ proxy: { password: string }; id: string; token: string }>(AUTH_FILE_PATH());

		expect(localEnvVars[APIFY_ENV_VARS.PROXY_PASSWORD]).toStrictEqual(auth.proxy.password);
		expect(localEnvVars[APIFY_ENV_VARS.USER_ID]).toStrictEqual(auth.id);
		expect(localEnvVars[APIFY_ENV_VARS.TOKEN]).toStrictEqual(auth.token);
		expect(localEnvVars.TEST_LOCAL).toStrictEqual(testEnvVars.TEST_LOCAL);

		const actOutputPath2 = joinPath(getLocalKeyValueStorePath(), 'two.json');
		const actOutput2 = loadJsonFileSync(actOutputPath2);
		expect(actOutput2).toStrictEqual('can play');
	});

	it('run purge stores', async () => {
		const input = {
			myInput: 'value',
		};
		const actInputPath = joinPath(getLocalKeyValueStorePath(), 'INPUT.json');
		const testJsonPath = joinPath(getLocalKeyValueStorePath(), 'TEST.json');

		writeJsonFileSync(actInputPath, input);

		let actCode = `
        import { Actor } from 'apify';

        Actor.main(async () => {
            await Actor.setValue('TEST', process.env);
            await Actor.pushData({aa: "bb" });
            const requestQueue = await Actor.openRequestQueue();
            await requestQueue.addRequest({ url: 'http://example.com/' });
        });
        `;
		writeFileSync(joinPath('src/main.js'), actCode, { flag: 'w' });

		await RunCommand.run([], import.meta.url);

		expect(existsSync(actInputPath)).toStrictEqual(true);
		expect(existsSync(testJsonPath)).toStrictEqual(true);
		expect(existsSync(joinPath(getLocalDatasetPath()))).toStrictEqual(true);
		expect(existsSync(joinPath(getLocalRequestQueuePath()))).toStrictEqual(true);

		actCode = `
        import { Actor } from 'apify';

        Actor.main(async () => {});
        `;
		writeFileSync(joinPath('src/main.js'), actCode, { flag: 'w' });

		await RunCommand.run(['--purge'], import.meta.url);

		expect(existsSync(actInputPath)).toStrictEqual(true);
		expect(existsSync(testJsonPath)).toStrictEqual(false);
		expect(existsSync(joinPath(getLocalDatasetPath()))).toStrictEqual(false);
		expect(existsSync(joinPath(getLocalRequestQueuePath()))).toStrictEqual(false);
	});

	it('run with purge works without storage folder', async () => {
		await rimrafPromised(getLocalStorageDir());
		try {
			await RunCommand.run(['--purge'], import.meta.url);
		} catch (err) {
			throw new Error('Can not run Actor without storage folder!');
		}
	});

	describe('input tests', () => {
		const actPath = joinPath('src/main.js');
		const inputSchemaPath = joinPath('INPUT_SCHEMA.json');
		const inputPath = joinPath(getLocalKeyValueStorePath(), 'INPUT.json');
		const outputPath = joinPath(getLocalKeyValueStorePath(), 'OUTPUT.json');
		const handPassedInput = JSON.stringify({ awesome: null });

		beforeAll(() => {
			writeFileSync(actPath, INPUT_SCHEMA_ACTOR_SRC, { flag: 'w' });
		});

		it('throws when required field is not provided', async () => {
			writeFileSync(inputPath, '{}', { flag: 'w' });
			copyFileSync(pathToMissingRequiredInputSchema, inputSchemaPath);

			const { error } = await captureOutput(async () => RunCommand.run([], import.meta.url));

			expect(error).toBeDefined();
			expect(error!.message).toMatch(/Field awesome is required/i);
		});

		it('throws when required field has wrong type', async () => {
			writeFileSync(inputPath, '{"awesome": 42}', { flag: 'w' });
			copyFileSync(pathToDefaultsInputSchema, inputSchemaPath);

			const { error } = await captureOutput(async () => RunCommand.run([], import.meta.url));

			expect(error).toBeDefined();
			expect(error!.message).toMatch(/Field awesome must be boolean/i);
		});

		it('throws when passing manual input, but local file has correct input', async () => {
			writeFileSync(inputPath, '{"awesome": true}', { flag: 'w' });
			copyFileSync(pathToDefaultsInputSchema, inputSchemaPath);

			const { error } = await captureOutput(async () =>
				RunCommand.run(['--input', handPassedInput], import.meta.url),
			);

			expect(error).toBeDefined();
			expect(error!.message).toMatch(/Field awesome must be boolean/i);
		});

		it('throws when input has default field of wrong type', async () => {
			writeFileSync(inputPath, '{"awesome": true, "help": 123}', { flag: 'w' });
			copyFileSync(pathToDefaultsInputSchema, inputSchemaPath);

			const { error } = await captureOutput(async () => RunCommand.run([], import.meta.url));

			expect(error).toBeDefined();
			expect(error!.message).toMatch(/Field help must be string/i);
		});

		it('throws when input has prefilled field of wrong type', async () => {
			writeFileSync(inputPath, '{"awesome": true, "help": 123}', { flag: 'w' });
			copyFileSync(pathToPrefillsInputSchema, inputSchemaPath);

			const { error } = await captureOutput(async () => RunCommand.run([], import.meta.url));

			expect(error).toBeDefined();
			expect(error!.message).toMatch(/Field help must be string/i);
		});

		it('automatically inserts missing defaulted fields', async () => {
			writeFileSync(inputPath, '{"awesome": true}', { flag: 'w' });
			copyFileSync(pathToDefaultsInputSchema, inputSchemaPath);

			await RunCommand.run([], import.meta.url);

			const output = loadJsonFileSync(outputPath);
			expect(output).toStrictEqual({ awesome: true, help: 'this_maze_is_not_meant_for_you' });
		});

		it('does not insert missing prefilled fields', async () => {
			writeFileSync(inputPath, '{"awesome": true}', { flag: 'w' });
			copyFileSync(pathToPrefillsInputSchema, inputSchemaPath);

			await RunCommand.run([], import.meta.url);

			const output = loadJsonFileSync(outputPath);
			expect(output).toStrictEqual({ awesome: true });
		});
	});
});


================================================
File: /bin/dev.cmd
================================================
@echo off

node "%~dp0\dev" %*


================================================
File: /bin/dev.js
================================================
import { execute } from '@oclif/core';
import { satisfies } from 'semver';

import { SUPPORTED_NODEJS_VERSION } from '../src/lib/consts.ts';
import { error } from '../src/lib/outputs.ts';

if (!satisfies(process.version, SUPPORTED_NODEJS_VERSION)) {
	error({
		message: `Apify CLI requires Node.js version ${SUPPORTED_NODEJS_VERSION}. Your current version is ${process.version}.`,
	});
	process.exit(1);
}

try {
	await execute({ development: true, dir: import.meta.url });
} catch (err) {
	const exitCode = err.oclif && err.oclif.exit !== undefined ? err.oclif.exit : 1;
	if (exitCode !== 0) {
		error(err.message);
		if (process.env.DEBUG) console.error(err);
		process.exit(exitCode);
	}
}


================================================
File: /bin/run.js
================================================
#!/usr/bin/env node

import { execute } from '@oclif/core';
import { satisfies } from 'semver';

import { SUPPORTED_NODEJS_VERSION } from '../dist/lib/consts.js';
import { error } from '../dist/lib/outputs.js';

if (!satisfies(process.version, SUPPORTED_NODEJS_VERSION)) {
	error({
		message: `Apify CLI requires Node.js version ${SUPPORTED_NODEJS_VERSION}. Your current version is ${process.version}.`,
	});
	process.exit(1);
}

try {
	await execute({ development: false, dir: import.meta.url });
} catch (err) {
	const exitCode = err.oclif && err.oclif.exit !== undefined ? err.oclif.exit : 1;
	if (exitCode !== 0) {
		error(err.message);
		if (process.env.DEBUG) console.error(err);
		process.exit(exitCode);
	}
}


================================================
File: /bin/dev.sh
================================================
#!/bin/bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"${DIR}"/../node_modules/.bin/tsx "${DIR}"/dev.js "$@"


================================================
File: /bin/run.cmd
================================================
@echo off

node "%~dp0\run" %*

================================================
File: /.yarnrc.yml
================================================
enableGlobalCache: true

nodeLinker: node-modules

plugins:
    - path: ./.yarn/plugins/postinstallDev.cjs
    - checksum: f8ce3a541a57481f6213647cfe7ac8555d87cb1fc23a73a102e64e12be07f603826d822f4d0285333400f0f15baed92510c33dcce75dde2953b2811e36efa012
      path: .yarn/plugins/@yarnpkg/plugin-git-hooks.cjs
      spec: "https://raw.githubusercontent.com/trufflehq/yarn-plugin-git-hooks/main/bundles/%40yarnpkg/plugin-git-hooks.js"

gitHooksPath: .github/hooks


================================================
File: /package.json
================================================
{
    "name": "apify-cli",
    "version": "0.21.0",
    "description": "Apify command-line interface (CLI) helps you manage the Apify cloud platform and develop, build, and deploy Apify Actors.",
    "exports": "./dist/index.js",
    "types": "./dist/index.d.ts",
    "type": "module",
    "scripts": {
        "dev": "tsx ./bin/dev.js",
        "test": "vitest run",
        "test-python": "vitest run -t '.*\\[python\\]'",
        "test:cucumber": "cross-env NODE_OPTIONS=\"--import tsx\" cucumber-js",
        "lint": "eslint src test .yarn/plugins --ext .ts,.cjs,.mjs",
        "lint:fix": "eslint src test .yarn/plugins --fix --ext .ts,.cjs,.mjs",
        "format": "biome format . && prettier --check \"**/*.{md,yml,yaml}\"",
        "format:fix": "biome format --write . && prettier --write \"**/*.{md,yml,yaml}\"",
        "clean": "rimraf dist",
        "build": "yarn clean && tsc && tsc -p tsconfig.typechecking.json",
        "postpack": "rimraf oclif.manifest.json",
        "prepack": "yarn build && oclif manifest && oclif readme && yarn update-docs",
        "update-docs": "oclif readme --readme-path=docs/reference.md",
        "postinstallDev": "yarn build && node ./bin/run.js check-version && node ./dist/lib/community.js"
    },
    "files": [
        "dist",
        "oclif.manifest.json",
        "bin"
    ],
    "bin": {
        "apify": "./bin/run.js"
    },
    "contributors": [
        "Jakub Drobník <jakub.drobnik@apify.com>",
        "Jan Curn <jan@apify.com>"
    ],
    "repository": {
        "type": "git",
        "url": "git+https://github.com/apify/apify-cli.git"
    },
    "keywords": [
        "apify",
        "client",
        "node",
        "command",
        "line",
        "bash"
    ],
    "author": {
        "name": "Apify",
        "email": "support@apify.com",
        "url": "https://www.apify.com"
    },
    "license": "Apache-2.0",
    "bugs": {
        "url": "https://github.com/apify/apify-cli/issues"
    },
    "homepage": "https://github.com/apify/apify-cli#readme",
    "engines": {
        "node": ">=18"
    },
    "dependencies": {
        "@apify/actor-templates": "~0.1.5",
        "@apify/consts": "~2.35.0",
        "@apify/input_schema": "~3.12.0",
        "@apify/utilities": "~2.11.0",
        "@crawlee/memory-storage": "~3.12.0",
        "@oclif/core": "~4.2.0",
        "@oclif/plugin-help": "~6.2.8",
        "@root/walk": "~1.1.0",
        "@sapphire/duration": "^1.1.2",
        "@sapphire/timestamp": "^1.0.3",
        "adm-zip": "~0.5.15",
        "ajv": "~8.17.1",
        "apify-client": "~2.11.0",
        "archiver": "~7.0.1",
        "axios": "~1.7.3",
        "chalk": "~5.4.0",
        "cli-table3": "^0.6.5",
        "computer-name": "~0.1.0",
        "configparser": "~0.3.10",
        "cors": "~2.8.5",
        "detect-indent": "~7.0.1",
        "escape-string-regexp": "~5.0.0",
        "express": "~4.21.0",
        "fs-extra": "^11.2.0",
        "globby": "~14.0.2",
        "handlebars": "~4.7.8",
        "inquirer": "~12.3.0",
        "is-ci": "~4.1.0",
        "is-online": "~11.0.0",
        "istextorbinary": "~9.5.0",
        "jju": "~1.4.0",
        "load-json-file": "~7.0.1",
        "lodash.clonedeep": "^4.5.0",
        "mime": "~4.0.4",
        "mixpanel": "~0.18.0",
        "open": "~10.1.0",
        "ow": "~2.0.0",
        "rimraf": "~6.0.1",
        "semver": "~7.6.3",
        "tiged": "~2.12.7",
        "underscore": "~1.13.7",
        "write-json-file": "~6.0.0"
    },
    "devDependencies": {
        "@apify/eslint-config": "^0.4.0",
        "@apify/eslint-config-ts": "^0.4.1",
        "@apify/tsconfig": "^0.1.0",
        "@biomejs/biome": "^1.8.3",
        "@crawlee/types": "^3.11.1",
        "@cucumber/cucumber": "^11.0.0",
        "@oclif/test": "^4.0.8",
        "@sapphire/result": "^2.6.6",
        "@types/adm-zip": "^0.5.5",
        "@types/archiver": "^6.0.2",
        "@types/chai": "^4.3.17",
        "@types/cors": "^2.8.17",
        "@types/express": "^4.17.21",
        "@types/fs-extra": "^11",
        "@types/inquirer": "^9.0.7",
        "@types/is-ci": "^3.0.4",
        "@types/jju": "^1.4.5",
        "@types/lodash.clonedeep": "^4",
        "@types/mime": "^4.0.0",
        "@types/node": "^22.0.0",
        "@types/semver": "^7.5.8",
        "@types/underscore": "^1.11.15",
        "@typescript-eslint/eslint-plugin": "^7.0.2",
        "@typescript-eslint/parser": "^7.0.2",
        "@yarnpkg/core": "^4.1.2",
        "apify": "^3.2.4",
        "chai": "^4.4.1",
        "cross-env": "^7.0.3",
        "eslint": "^8.57.0",
        "eslint-config-prettier": "^9.1.0",
        "execa": "^9.3.0",
        "lint-staged": "^15.2.8",
        "mock-stdin": "^1.0.0",
        "oclif": "^4.14.15",
        "prettier": "^3.3.3",
        "tsx": "^4.16.5",
        "typescript": "^5.5.4",
        "vitest": "^2.1.5"
    },
    "oclif": {
        "bin": "apify",
        "dirname": "apify",
        "commands": "./dist/commands",
        "plugins": [
            "@oclif/plugin-help"
        ],
        "hooks": {
            "init": [
                "./dist/hooks/init"
            ],
            "prerun": [
                "./dist/hooks/deprecations"
            ]
        },
        "helpClass": "./dist/lib/apify-oclif-help",
        "additionalHelpFlags": [
            "-h"
        ],
        "additionalVersionFlags": [
            "-v"
        ],
        "topicSeparator": " "
    },
    "volta": {
        "node": "22.12.0",
        "yarn": "4.5.3"
    },
    "packageManager": "yarn@4.5.3",
    "lint-staged": {
        "*": "biome format --write --no-errors-on-unmatched",
        "*.{mjs,js,ts}": "eslint --fix --ext mjs,js,ts",
        "*.md": "prettier --write"
    }
}


================================================
File: /.nvmrc
================================================
22.12.0


================================================
File: /website/sidebars.js
================================================
module.exports = [
    [
        {
            type: 'doc',
            id: 'index',
            label: 'Apify CLI',
        },
        {
            type: 'doc',
            id: 'installation',
            label: 'Installation',
        },
        {
            type: 'doc',
            id: 'vars',
            label: 'Environment variables',
        },
        {
            type: 'doc',
            id: 'reference',
            label: 'Command reference',
        },
        {
            type: 'doc',
            id: 'integrating-scrapy',
            label: 'Integrating Scrapy',
        },
        {
            type: 'doc',
            id: 'troubleshooting',
            label: 'Troubleshooting',
        },
        {
            type: 'doc',
            id: 'changelog',
            label: 'Changelog',
        },
    ],
];


================================================
File: /website/tsconfig.eslint.json
================================================
{
	"extends": "@apify/tsconfig",
	"compilerOptions": {
		"jsx": "preserve"
	},
	"include": [
		"src/**/*.js",
		"src/**/*.ts",
		"src/**/*.jsx",
		"src/**/*.tsx"
	]
}


================================================
File: /website/sitePlugin.js
================================================
module.exports = function () {
    return {
        name: 'custom-docusaurus-plugin',
        // eslint-disable-next-line
        configureWebpack(config, isServer, utils) {
            return {
                resolve: {
                    alias: {
                        path: require.resolve('path-browserify'),
                    },
                    fallback: {
                        fs: false,
                    },
                },
            };
        },
    };
};


================================================
File: /website/.gitignore
================================================
*.log
*.pid
*.seed
.DS_Store
lib
coverage
.nyc_output
logs
pids
.idea
.vscode
tmp
jsconfig.json
types
docs/api
docs/typedefs
.history
.docusaurus
tsconfig.tsbuildinfo
apify_storage
crawlee_storage
storage
.turbo

# Yarn files
.yarn/install-state.gz
.yarn/build-state.yml


================================================
File: /website/.eslintrc.json
================================================
{
    "extends": [
        "@apify/eslint-config-ts",
        "plugin:react/recommended",
        "plugin:react-hooks/recommended"
    ],
    "parserOptions": {
        "project": "./tsconfig.eslint.json",
        "ecmaFeatures": {
            "jsx": true
        },
        "ecmaVersion": 2020
    },
    "env": {
        "browser": true
    },
    "settings": {
        "react": {
            "version": "detect"
        }
    },
    "root": true,
    "rules": {
        "quote-props": ["error", "consistent"]
    }
}


================================================
File: /website/versions.json
================================================
[
  "0.20"
]


================================================
File: /website/.yarnrc.yml
================================================
enableGlobalCache: true

nodeLinker: node-modules


================================================
File: /website/tools/docs-prettier.config.js
================================================
/**
 * @type {import('prettier').Options}
 */
module.exports = {
    parser: 'markdown',
    arrowParens: 'avoid',
    trailingComma: 'all',
    singleQuote: true,
    tabWidth: 4,
    printWidth: 150,
    proseWrap: 'always',
};


================================================
File: /website/tools/utils/createHref.js
================================================
/* eslint-disable max-len */
/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * The SVG used below is used from docusaurus, which is licensed under the MIT license found in the
 * LICENSE file located at: https://github.com/facebook/docusaurus
 */

exports.createHref = (url, label) => {
    return `<a href="${url}" target="_blank" class="footer__link-item">
        <span>
            ${label}
            <svg
                width="13.5"
                height="13.5"
                aria-hidden="true"
                viewBox="0 0 24 24"
                style="margin-left: 0.3rem; position: relative; top: 1px;"
                >
                <path fill="currentColor" d="M21 13v10h-21v-19h12v2h-10v15h17v-8h2zm3-12h-10.988l4.035 4-6.977 7.07 2.828 2.828 6.977-7.07 4.125 4.172v-11z">
                </path>
            </svg>
        </span>
    </a>`;
};


================================================
File: /website/tools/utils/externalLink.js
================================================
const { parse } = require('url');

const visit = import('unist-util-visit').then((m) => m.visit);

const internalUrls = ['sdk.apify.com'];

/**
 * @param {import('url').UrlWithStringQuery} href
 */
function isInternal(href) {
    return internalUrls.some(
        (internalUrl) => href.host === internalUrl
            || (!href.protocol && !href.host && (href.pathname || href.hash)),
    );
}

/**
 * @type {import('unified').Plugin}
 */
exports.externalLinkProcessor = () => {
    return async (tree) => {
        (await visit)(tree, 'element', (node) => {
            if (
                node.tagName === 'a'
                && node.properties
                && typeof node.properties.href === 'string'
            ) {
                const href = parse(node.properties.href);

                if (!isInternal(href)) {
                    node.properties.target = '_blank';
                    node.properties.rel = 'noopener';
                } else {
                    node.properties.target = null;
                    node.properties.rel = null;
                }
            }
        });
    };
};


================================================
File: /website/package.json
================================================
{
    "scripts": {
        "examples": "docusaurus-examples",
        "start": "rimraf .docusaurus && docusaurus start",
        "build": "rimraf .docusaurus && docusaurus build",
        "publish-gh-pages": "docusaurus-publish",
        "write-translations": "docusaurus write-translations",
        "version": "docusaurus version",
        "rename-version": "docusaurus rename-version",
        "prettify": "prettier --write --config ./tools/docs-prettier.config.js ../docs/guides/*.md",
        "swizzle": "docusaurus swizzle",
        "deploy": "rimraf .docusaurus && docusaurus deploy",
        "docusaurus": "docusaurus"
    },
    "devDependencies": {
        "@apify/eslint-config-ts": "^0.4.0",
        "@apify/tsconfig": "^0.1.0",
        "@types/react": "^18.0.0",
        "@typescript-eslint/eslint-plugin": "^7.0.0",
        "@typescript-eslint/parser": "^7.0.0",
        "eslint": "^8.53.0",
        "eslint-plugin-react": "^7.33.2",
        "eslint-plugin-react-hooks": "^5.0.0",
        "path-browserify": "^1.0.1",
        "prettier": "^3.0.3",
        "rimraf": "^6.0.0"
    },
    "dependencies": {
        "@apify/docs-theme": "^1.0.148",
        "@docusaurus/core": "^3.5.2",
        "@docusaurus/plugin-client-redirects": "^3.5.2",
        "@docusaurus/preset-classic": "^3.5.2",
        "clsx": "^1.2.1",
        "docusaurus-gtm-plugin": "^0.0.2",
        "prop-types": "^15.8.1",
        "raw-loader": "^4.0.2",
        "react": "^18.3.1",
        "react-dom": "^18.3.1",
        "unist-util-visit": "^5.0.0"
    },
    "volta": {
        "node": "22.12.0",
        "yarn": "4.5.3"
    },
    "packageManager": "yarn@4.5.3"
}


================================================
File: /website/versioned_docs/version-0.20/vars.md
================================================
---
sidebar_label: Environment variables
title: Environment variables
---

There are two options how you can set up environment variables for Actors.

### Set up environment variables in `.actor/actor.json`

All keys from `env` will be set as environment variables into Apify platform after you push Actor to Apify. Current values on Apify will be overridden.

```json
{
  "actorSpecification": 1,
  "name": "dataset-to-mysql",
  "version": "0.1",
  "buildTag": "latest",
  "environmentVariables": {
    "MYSQL_USER": "my_username",
    "MYSQL_PASSWORD": "@mySecretPassword"
  }
}
```

### Set up environment variables in Apify Console

In [Apify Console](https://console.apify.com/actors) select your Actor, you can set up variables into Source tab.
After setting up variables in the app, remove the `environmentVariables` from `.actor/actor.json`. Otherwise, variables from `.actor/actor.json` will override variables in the app.

```json
{
  "actorSpecification": 1,
  "name": "dataset-to-mysql",
  "version": "0.1",
  "buildTag": "latest"
}
```

#### How to set secret environment variables in `.actor/actor.json`

CLI provides commands to manage secrets environment variables. Secrets are stored to the `~/.apify` directory.
You can add a new secret using the command:

```bash
apify secrets add mySecretPassword pwd1234
```

After adding a new secret you can use the secret in `.actor/actor.json`.

```text
{
    "actorSpecification": 1,
    "name": "dataset-to-mysql",
    ...
    "environmentVariables": {
      "MYSQL_PASSWORD": "@mySecretPassword"
    },
    ...
}
```

### Need help?

To see all CLI commands simply run:

```bash
apify help
```

To get information about a specific command run:

```bash
apify help COMMAND
```

Still haven't found what you were looking for? Please go to [Apify Help center](https://www.apify.com/help)
or [contact us](https://www.apify.com/contact).


================================================
File: /website/versioned_docs/version-0.20/integrating-scrapy.md
================================================
---
title: Integrating Scrapy projects
description: Learn how to run Scrapy projects as Apify Actors and deploy them on the Apify platform.
sidebar_label: Integrating Scrapy projects
---

[Scrapy](https://scrapy.org/) is a widely used open-source web scraping framework for Python. Scrapy projects can now be executed on the Apify platform using our dedicated wrapping tool. This tool allows users to transform their Scrapy projects into [Apify Actors](https://docs.apify.com/platform/actors) with just a few simple commands.

## Getting started

### Install Apify CLI

To run the migration tool, you need to have the Apify CLI installed. You can install it using Homebrew with the following command:

```bash showLineNumbers
brew install apify-cli
```

Alternatively, you can install it using NPM with the following command:

```bash showLineNumbers
npm i -g apify-cli
```

In case of any issues, please refer to the [installation guide](./installation.md).

## Actorization of your existing Scrapy spider

Assuming your Scrapy project is set up, navigate to the project root where the `scrapy.cfg` file is located.

```bash showLineNumbers
cd your_scraper
```

Verify the directory contents to ensure the correct location.

```bash showLineNumbers
$ ls -R
.:
your_scraper  README.md  requirements.txt  scrapy.cfg

./your_scraper:
__init__.py  items.py  __main__.py  main.py  pipelines.py  settings.py  spiders

./your_scraper/spiders:
your_spider.py  __init__.py
```

To convert your Scrapy project into an Apify Actor, initiate the wrapping process by executing the following command:

```bash showLineNumbers
apify init
```

The script will prompt you with a series of questions. Upon completion, the output might resemble the following:

```bash showLineNumbers
Info: The current directory looks like a Scrapy project. Using automatic project wrapping.
? Enter the Scrapy BOT_NAME (see settings.py): books_scraper
? What folder are the Scrapy spider modules stored in? (see SPIDER_MODULES in settings.py): books_scraper.spiders
? Pick the Scrapy spider you want to wrap: BookSpider (/home/path/to/actor-scrapy-books-example/books_scraper/spiders/book.py)
Info: Downloading the latest Scrapy wrapper template...
Info: Wrapping the Scrapy project...
Success: The Scrapy project has been wrapped successfully.
```

For example, here is a [source code](https://github.com/apify/actor-scrapy-books-example) of an actorized Scrapy project, and [here](https://apify.com/vdusek/scrapy-books-example) the corresponding Actor in Apify Store.

### Run the Actor locally

Create a Python virtual environment by running:

```bash showLineNumbers
python -m virtualenv .venv
```

Activate the virtual environment:

```bash showLineNumbers
source .venv/bin/activate
```

Install Python dependencies using the provided requirements file named `requirements_apify.txt`. Ensure these requirements are installed before executing your project as an Apify Actor locally. You can put your own dependencies there as well.

```bash showLineNumbers
pip install -r requirements-apify.txt [-r requirements.txt]
```

Finally execute the Apify Actor.

```bash showLineNumbers
apify run [--purge]
```

If [ActorDatasetPushPipeline](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/pipelines.py) is configured, the Actor's output will be stored in the `storage/datasets/default/` directory.

### Run the scraper as Scrapy project

The project remains executable as a Scrapy project.

```bash showLineNumbers
scrapy crawl your_spider -o books.json
```

## Deploy on Apify

### Log in to Apify

You will need to provide your [Apify API Token](https://console.apify.com/settings/integrations) to complete this action.

```bash showLineNumbers
apify login
```

### Deploy your Actor

This command will deploy and build the Actor on the Apify platform. You can find your newly created Actor under [Actors -> My Actors](https://console.apify.com/actors?tab=my).

```bash showLineNumbers
apify push
```

## What the wrapping process does

The initialization command enhances your project by adding necessary files and updating some of them while preserving its functionality as a typical Scrapy project. The additional requirements file, named `requirements_apify.txt`, includes the Apify Python SDK and other essential requirements. The `.actor/` directory contains basic configuration of your Actor. We provide two new Python files [main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py) and [\_\_main\_\_.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/__main__.py), where we encapsulate the Scrapy project within an Actor. We also import and use there a few Scrapy components from our [Python SDK](https://github.com/apify/apify-sdk-python/tree/master/src/apify/scrapy). These components facilitate the integration of the Scrapy projects with the Apify platform. Further details about these components are provided in the following subsections.

### Scheduler

The [scheduler](https://docs.scrapy.org/en/latest/topics/scheduler.html) is a core component of Scrapy responsible for receiving and providing requests to be processed. To leverage the [Apify request queue](https://docs.apify.com/platform/storage/request-queue) for storing requests, a custom scheduler becomes necessary. Fortunately, Scrapy is a modular framework, allowing the creation of custom components. As a result, we have implemented the [ApifyScheduler](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/scheduler.py). When using the Apify CLI wrapping tool, the scheduler is configured in the [src/main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py) file of your Actor.

### Dataset push pipeline

[Item pipelines](https://docs.scrapy.org/en/latest/topics/item-pipeline.html) are used for the processing of the results produced by your spiders. To handle the transmission of result data to the [Apify dataset](https://docs.apify.com/platform/storage/dataset), we have implemented the [ActorDatasetPushPipeline](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/pipelines.py). When using the Apify CLI wrapping tool, the pipeline is configured in the [src/main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py) file of your Actor. It is assigned the highest integer value (1000), ensuring its execution as the final step in the pipeline sequence.

### Retry middleware

[Downloader middlewares](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html) are a way how to hook into Scrapy's request/response processing. Scrapy comes with various default middlewares, including the [RetryMiddleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#module-scrapy.downloadermiddlewares.retry), designed to handle retries for requests that may have failed due to temporary issues. When integrating with the [Apify request queue](https://docs.apify.com/platform/storage/request-queue), it becomes necessary to enhance this middleware to facilitate communication with the request queue marking the requests either as handled or ready for a retry. When using the Apify CLI wrapping tool, the default `RetryMiddleware` is disabled, and [ApifyRetryMiddleware](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/middlewares/apify_retry.py) takes its place. Configuration for the middlewares is established in the [src/main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py) file of your Actor.

### HTTP proxy middleware

Another default Scrapy [downloader middleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html) that requires replacement is [HttpProxyMiddleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#module-scrapy.downloadermiddlewares.httpproxy). To utilize the use of proxies managed through the Apify [ProxyConfiguration](https://github.com/apify/apify-sdk-python/blob/master/src/apify/proxy_configuration.py), we provide [ApifyHttpProxyMiddleware](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/middlewares/apify_proxy.py). When using the Apify CLI wrapping tool, the default `HttpProxyMiddleware` is disabled, and [ApifyHttpProxyMiddleware](https://github.com/apify/apify-sdk-python/blob/master/src/apify/scrapy/middlewares/apify_proxy.py) takes its place. Additionally, inspect the [.actor/input_schema.json](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/.actor/input_schema.json) file, where proxy configuration is specified as an input property for your Actor. The processing of this input is carried out together with the middleware configuration in [src/main.py](https://github.com/apify/actor-templates/blob/master/templates/python-scrapy/src/main.py).

## Known limitations

There are some known limitations of running the Scrapy projects on Apify platform we are aware of.

### Asynchronous code in spiders and other components

Scrapy asynchronous execution is based on the [Twisted](https://twisted.org/) library, not the
[AsyncIO](https://docs.python.org/3/library/asyncio.html), which brings some complications on the table.

Due to the asynchronous nature of the Actors, all of their code is executed as a coroutine inside the `asyncio.run`.
In order to execute Scrapy code inside an Actor, following the section
[Run Scrapy from a script](https://docs.scrapy.org/en/latest/topics/practices.html?highlight=CrawlerProcess#run-scrapy-from-a-script)
from the official Scrapy documentation, we need to invoke a
[`CrawlProcess.start`](https://github.com/scrapy/scrapy/blob/2.11.0/scrapy/crawler.py#L393:L427)
method. This method triggers Twisted's event loop, also known as a reactor.
Consequently, Twisted's event loop is executed within AsyncIO's event loop.
On top of that, when employing AsyncIO code in spiders or other components, it necessitates the creation of a new
AsyncIO event loop, within which the coroutines from these components are executed. This means there is
an execution of the AsyncIO event loop inside the Twisted event loop inside the AsyncIO event loop.

We have resolved this issue by leveraging the [nest-asyncio](https://pypi.org/project/nest-asyncio/) library,
enabling the execution of nested AsyncIO event loops. For executing a coroutine within a spider or other component,
it is recommended to use Apify's instance of the nested event loop. Refer to the code example below or derive
inspiration from Apify's Scrapy components, such as the
[ApifyScheduler](https://github.com/apify/apify-sdk-python/blob/v1.5.0/src/apify/scrapy/scheduler.py#L114).

```python showLineNumbers
from apify.scrapy.utils import nested_event_loop

...

# Coroutine execution inside a spider
nested_event_loop.run_until_complete(my_coroutine())
```

### More spiders per Actor

It is recommended to execute only one Scrapy spider per Apify Actor.

Mapping more Scrapy spiders to a single Apify Actor does not make much sense. We would have to create a separate
instace of the [request queue](https://docs.apify.com/platform/storage/request-queue) for every spider.
Also, every spider can produce a different output resulting in a mess in an output
[dataset](https://docs.apify.com/platform/storage/dataset). A solution for this could be to store an output
of every spider to a different [key-value store](https://docs.apify.com/platform/storage/key-value-store). However,
a much more simple solution to this problem would be to just have a single spider per Actor.

If you want to share common Scrapy components (middlewares, item pipelines, ...) among more spiders (Actors), you
can use a dedicated Python package containing your components and install it to your Actors environment. The
other solution to this problem could be to have more spiders per Actor, but keep only one spider run per Actor.
What spider is going to be executed in an Actor run can be specified in the
[input schema](https://docs.apify.com/academy/deploying-your-code/input-schema).

## Additional links

- [Scrapy Books Example Actor](https://apify.com/vdusek/scrapy-books-example)
- [Python Actor Scrapy template](https://apify.com/templates/python-scrapy)
- [Apify SDK for Python](https://docs.apify.com/sdk/python)
- [Apify platform](https://docs.apify.com/platform)
- [Join our developer community on Discord](https://discord.com/invite/jyEM2PRvMU)

> We welcome any feedback! Please feel free to contact us at [python@apify.com](mailto:python@apify.com). Thank you for your valuable input.


================================================
File: /website/versioned_docs/version-0.20/troubleshooting.md
================================================
---
sidebar_label: Troubleshooting
title: Troubleshooting
---

For general support, reach out to us at [apify.com/contact](https://apify.com/contact).

If you believe you are encountering a bug, file it on [GitHub](https://github.com/apify/apify-cli/issues/new).


================================================
File: /website/versioned_docs/version-0.20/changelog.md
================================================
---
title: Changelog
sidebar_label: Changelog
toc_max_heading_level: 2
---

## [v0.20.11](https://github.com/apify/apify-cli/releases/tag/v0.20.11)

#### What's Changed

- fix: scrapy wrapping being broken due to ESM migration ([#686](https://github.com/apify/apify-cli/pull/686)) by [@vladfrangu](https://github.com/vladfrangu)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.10...v0.20.11

## [v0.20.10](https://github.com/apify/apify-cli/releases/tag/v0.20.10)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.9...v0.20.10

## [v0.20.9](https://github.com/apify/apify-cli/releases/tag/v0.20.9)

#### What's Changed

- fix: emit warning if input.json is modified during run and prefilled with defaults ([#672](https://github.com/apify/apify-cli/pull/672)) by [@vladfrangu](https://github.com/vladfrangu)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.8...v0.20.9

## [v0.20.8](https://github.com/apify/apify-cli/releases/tag/v0.20.8)

#### What's Changed

- Reverted the empty namespaces that were added in the previous release
- fix: look for lowercase input schema in default paths ([#647](https://github.com/apify/apify-cli/pull/647)) by [@mvolfik](https://github.com/mvolfik)
- Increase the minimum Python version to 3.9, in line with Apify SDK

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.7...v0.20.8

## [v0.20.7](https://github.com/apify/apify-cli/releases/tag/v0.20.7)

#### What's Changed

- fix: auto-set `apify run` `INPUT.json` only with values that have defaults by [@vladfrangu](https://github.com/vladfrangu) in [#641](https://github.com/apify/apify-cli/pull/641)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.6...v0.20.7

## [v0.20.6](https://github.com/apify/apify-cli/releases/tag/v0.20.6)

#### What's Changed

- fix: ensure input kvs path exists when calling `apify run` by [@vladfrangu](https://github.com/vladfrangu) in [#625](https://github.com/apify/apify-cli/pull/625)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.5...v0.20.6

## [v0.20.5](https://github.com/apify/apify-cli/releases/tag/v0.20.5)

#### What's Changed

- fix: print path to invalid `actor.json` when an invalid file is found by [@vladfrangu](https://github.com/vladfrangu) in [#618](https://github.com/apify/apify-cli/pull/618)
- fix: passing the item via stdin to `actor push-data` works again by [@vladfrangu](https://github.com/vladfrangu) in [#617](https://github.com/apify/apify-cli/pull/617)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.4...v0.20.5

## [v0.20.4](https://github.com/apify/apify-cli/releases/tag/v0.20.4)

#### What's Changed

- feat: printing dataset result for `call` command by [@vladfrangu](https://github.com/vladfrangu) in [#614](https://github.com/apify/apify-cli/pull/614)

#### New Contributors

- @netmilk made their first contribution in [#609](https://github.com/apify/apify-cli/pull/609)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.3...v0.20.4

## [v0.20.3](https://github.com/apify/apify-cli/releases/tag/v0.20.3)

#### What's Changed

- fix(call): support calling with bare ids by [@vladfrangu](https://github.com/vladfrangu) in [#613](https://github.com/apify/apify-cli/pull/613)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.2...v0.20.3

## [v0.20.2](https://github.com/apify/apify-cli/releases/tag/v0.20.2)

#### What's Changed

- fix: run scripts not printing unsupported node versions rightly by [@vladfrangu](https://github.com/vladfrangu) in [#589](https://github.com/apify/apify-cli/pull/589)
- fix: run command validating inputs caused inputs to not work in crawlee projects by [@vladfrangu](https://github.com/vladfrangu) in [#591](https://github.com/apify/apify-cli/pull/591)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.20.0...v0.20.2

## [](https://github.com/apify/apify-cli/releases/tag/v0.20.0)

#### What's Changed

- feat: add a troubleshooting section to the root help screen by [@tobice](https://github.com/tobice) in [#491](https://github.com/apify/apify-cli/pull/491)
- feat: Better copy and docs by [@jancurn](https://github.com/jancurn) in [#494](https://github.com/apify/apify-cli/pull/494)
- fix: prompt for new folder name when existing folder is used with `apify create` by [@vladfrangu](https://github.com/vladfrangu) in [#504](https://github.com/apify/apify-cli/pull/504)
- feat: Warn user there's newer Actor version on the platform by [@HonzaTuron](https://github.com/HonzaTuron) in [#506](https://github.com/apify/apify-cli/pull/506)
- feat: use login-new as default login method by [@HonzaTuron](https://github.com/HonzaTuron) in [#508](https://github.com/apify/apify-cli/pull/508)
- feat: support spaces and `:` for subcommands by [@vladfrangu](https://github.com/vladfrangu) in [#521](https://github.com/apify/apify-cli/pull/521)
- feat: prevent old node from running CLI by [@vladfrangu](https://github.com/vladfrangu) in [#522](https://github.com/apify/apify-cli/pull/522)
- feat: different exit codes for different errors by [@vladfrangu](https://github.com/vladfrangu) in [#520](https://github.com/apify/apify-cli/pull/520)
- feat: --no-optional for create command by [@vladfrangu](https://github.com/vladfrangu) in [#524](https://github.com/apify/apify-cli/pull/524)
- feat: support calling actors with bare names by [@vladfrangu](https://github.com/vladfrangu) in [#538](https://github.com/apify/apify-cli/pull/538)
- feat: support running other entrypoints with injected Apify environment variables by [@vladfrangu](https://github.com/vladfrangu) in [#539](https://github.com/apify/apify-cli/pull/539)
- fix: always enable crawlee storage purging when `--purge` is provided, even in non-crawlee-detected envs by [@vladfrangu](https://github.com/vladfrangu) in [#543](https://github.com/apify/apify-cli/pull/543)
- feat: Setup Smartlook for CLI docs by [@HonzaTuron](https://github.com/HonzaTuron) in [#544](https://github.com/apify/apify-cli/pull/544)
- fix: prevent running `apify push` from non-actor-looking folders by [@vladfrangu](https://github.com/vladfrangu) in [#537](https://github.com/apify/apify-cli/pull/537)
- fix: purge working in python again by [@vladfrangu](https://github.com/vladfrangu) in [#548](https://github.com/apify/apify-cli/pull/548)
- fix: deprecate `vis` command in favor of `validate-schema` by [@vladfrangu](https://github.com/vladfrangu) in [#556](https://github.com/apify/apify-cli/pull/556)
- fix: always try to get a remote storage if IS_AT_HOME is true by [@vladfrangu](https://github.com/vladfrangu) in [#557](https://github.com/apify/apify-cli/pull/557)
- feat: task run, actor call, deprecate top level call by [@vladfrangu](https://github.com/vladfrangu) in [#558](https://github.com/apify/apify-cli/pull/558)
- fix: print most information to stderr in preparation of future integrations by [@vladfrangu](https://github.com/vladfrangu) in [#570](https://github.com/apify/apify-cli/pull/570)
- feat: Update api token links by [@valekjo](https://github.com/valekjo) in [#578](https://github.com/apify/apify-cli/pull/578)
- feat: validate input on run by [@vladfrangu](https://github.com/vladfrangu) in [#560](https://github.com/apify/apify-cli/pull/560)
- feat: call with inputs by [@vladfrangu](https://github.com/vladfrangu) in [#577](https://github.com/apify/apify-cli/pull/577)
- chore: migrate to TypeScript and Oclif 3 by [@vladfrangu](https://github.com/vladfrangu) in [#477](https://github.com/apify/apify-cli/pull/477)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.19.5...v0.20.0

## [v0.19.5](https://github.com/apify/apify-cli/releases/tag/v0.19.5)

#### What's Changed

- fix: CLI on Windows throwing EINVAL errors with latest node 18/20/22 by [@vladfrangu](https://github.com/vladfrangu)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.19.4...v0.19.5

## [v0.19.4](https://github.com/apify/apify-cli/releases/tag/v0.19.4)

#### What's Changed

- fix: make `run --purge` work again for Python projects by [@vladfrangu](https://github.com/vladfrangu)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.19.3...v0.19.4

## [](https://github.com/apify/apify-cli/releases/tag/v0.19.3)

#### What's Changed

- fix: always enable crawlee storage purging when `--purge` is provided even in non-crawlee-detected envs by [@vladfrangu](https://github.com/vladfrangu)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.19.2...v0.19.3

## [v0.19.2](https://github.com/apify/apify-cli/releases/tag/v0.19.2)

#### What's Changed

- feat: validate the Actor name during init by [@barjin](https://github.com/barjin) in [#450](https://github.com/apify/apify-cli/pull/450)
- feat: extend success command on create by [@HonzaTuron](https://github.com/HonzaTuron) in [#466](https://github.com/apify/apify-cli/pull/466)
- fix: axios v1 and new client breaking cli by [@vladfrangu](https://github.com/vladfrangu) in [#481](https://github.com/apify/apify-cli/pull/481)

#### New Contributors

- @vdusek made their first contribution in [#439](https://github.com/apify/apify-cli/pull/439)
- @TC-MO made their first contribution in [#468](https://github.com/apify/apify-cli/pull/468)
- @honzajavorek made their first contribution in [#472](https://github.com/apify/apify-cli/pull/472)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.19.1...v0.19.2

## [v0.19.1](https://github.com/apify/apify-cli/releases/tag/v0.19.1)

#### What's Changed

- fix: restore fallback behaviour for `apify run` in Scrapy projects by [@barjin](https://github.com/barjin) in [#437](https://github.com/apify/apify-cli/pull/437)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.19.0...v0.19.1

## [v0.19.0](https://github.com/apify/apify-cli/releases/tag/v0.19.0)

#### What's Changed

- feat: Auto-update `apify-cli` Homebrew formula in `homebrew-core` by [@fnesveda](https://github.com/fnesveda) in [#387](https://github.com/apify/apify-cli/pull/387)
- fix: spelling in helpers by [@barjin](https://github.com/barjin) in [#389](https://github.com/apify/apify-cli/pull/389)
- feat: `apify init` wraps Scrapy projects with Apify middleware by [@barjin](https://github.com/barjin) in [#393](https://github.com/apify/apify-cli/pull/393)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.18.1...v0.19.0

## [v0.18.1](https://github.com/apify/apify-cli/releases/tag/v0.18.1)

#### What's Changed

##### Fixes

- Fixed `actor:push-data` and `actor:set-value` commands by [@drobnikj](https://github.com/drobnikj) in [#386](https://github.com/apify/apify-cli/pull/386)

##### Documentation changes

- Updated Homebrew installation instructions by [@fnesveda](https://github.com/fnesveda) in [#385](https://github.com/apify/apify-cli/pull/385)
- Minor rewording by [@jancurn](https://github.com/jancurn) in [#383](https://github.com/apify/apify-cli/pull/383)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.18.0...v0.18.1

## [v0.18.0](https://github.com/apify/apify-cli/releases/tag/v0.18.0)

#### What's Changed

- feat(create, init): create INPUT.json from input_schema prefills by [@nguyeda1](https://github.com/nguyeda1) in [#379](https://github.com/apify/apify-cli/pull/379)
- feat: Use actor/apify env vars instead of old `ENV_VARS` by [@jirimoravcik](https://github.com/jirimoravcik) in [#381](https://github.com/apify/apify-cli/pull/381)
- chore: Bump version to 0.18.0 by [@jirimoravcik](https://github.com/jirimoravcik) in [#382](https://github.com/apify/apify-cli/pull/382)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.17.0...v0.18.0

## [v0.17.0](https://github.com/apify/apify-cli/releases/tag/v0.17.0)

#### What's Changed

- BREAKING CHANGE: Telemetry data collection by [@drobnikj](https://github.com/drobnikj) in [#362](https://github.com/apify/apify-cli/pull/362)
- chore: Fix docs reference by [@drobnikj](https://github.com/drobnikj) in [#375](https://github.com/apify/apify-cli/pull/375)
- fix: Folder path creation by [@HonzaTuron](https://github.com/HonzaTuron) in [#376](https://github.com/apify/apify-cli/pull/376)
- feat(create): Merge local development instructions into README by [@nguyeda1](https://github.com/nguyeda1) in [#372](https://github.com/apify/apify-cli/pull/372)

#### New Contributors

- @nguyeda1 made their first contribution in [#372](https://github.com/apify/apify-cli/pull/372)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.16.2...v0.17.0

## [v0.16.2](https://github.com/apify/apify-cli/releases/tag/v0.16.2)

#### What's Changed

- chore: Use new workflow secrets by [@fnesveda](https://github.com/fnesveda) in [#361](https://github.com/apify/apify-cli/pull/361)
- feat: Add community message by [@HonzaTuron](https://github.com/HonzaTuron) in [#363](https://github.com/apify/apify-cli/pull/363)
- fix: Use the right exit code on error by [@fnesveda](https://github.com/fnesveda) in [#364](https://github.com/apify/apify-cli/pull/364)
- feat(push): Allow disabling of the prompt mechanism via flag/CI by [@vladfrangu](https://github.com/vladfrangu) in [#365](https://github.com/apify/apify-cli/pull/365)
- fix(push): Correctly check if in CI env to skip prompt by [@vladfrangu](https://github.com/vladfrangu) in [#366](https://github.com/apify/apify-cli/pull/366)
- fix: Fix unit tests by [@fnesveda](https://github.com/fnesveda) in [#371](https://github.com/apify/apify-cli/pull/371)
- feat(app): Add apify pull by [@HonzaTuron](https://github.com/HonzaTuron) in [#360](https://github.com/apify/apify-cli/pull/360)

#### New Contributors

- @vladfrangu made their first contribution in [#365](https://github.com/apify/apify-cli/pull/365)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.16.1...v0.16.2

## [v0.16.1](https://github.com/apify/apify-cli/releases/tag/v0.16.1)

#### What's Changed

- Fix `apify create` on Node 19+, add Node 20 to CI test roster by [@fnesveda](https://github.com/fnesveda) in [#359](https://github.com/apify/apify-cli/pull/359)

## [v0.16.0](https://github.com/apify/apify-cli/releases/tag/v0.16.0)

#### What's Changed

##### New features

- Added option to open actor detail in Apify Console after successful `apify push` by [@HonzaTuron](https://github.com/HonzaTuron) in [#353](https://github.com/apify/apify-cli/pull/353)

##### Fixes

- Stopped adding `apify_storage` to .gitignore if it already is there by [@fnesveda](https://github.com/fnesveda) in [#355](https://github.com/apify/apify-cli/pull/355)
- Fixed extracting some template archives by [@mvolfik](https://github.com/mvolfik) in [#358](https://github.com/apify/apify-cli/pull/358)
- Improved log messages for different build statuses by [@fnesveda](https://github.com/fnesveda) in [#350](https://github.com/apify/apify-cli/pull/350)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.15.1...v0.16.0

## [v0.15.1](https://github.com/apify/apify-cli/releases/tag/v0.15.1)

#### What's Changed

- Added a post-create message to Python actors by [@fnesveda](https://github.com/fnesveda) in [#349](https://github.com/apify/apify-cli/pull/349)
- Updated the `apify run` help to not be so Node-specific by [@fnesveda](https://github.com/fnesveda) in [#347](https://github.com/apify/apify-cli/pull/347)
- Started using correct "omit optional dependencies" argument based on NPM version by [@fnesveda](https://github.com/fnesveda) in [#346](https://github.com/apify/apify-cli/pull/346)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.15.0...v0.15.1

## [v0.15.0](https://github.com/apify/apify-cli/releases/tag/v0.15.0)

#### New features

- Apify Console login integration in `apify login-new` by [@fnesveda](https://github.com/fnesveda) in [#302](https://github.com/apify/apify-cli/pull/302)
- Preparations for release on Homebrew by [@fnesveda](https://github.com/fnesveda) in [#341](https://github.com/apify/apify-cli/pull/341), [#342](https://github.com/apify/apify-cli/pull/342), [#343](https://github.com/apify/apify-cli/pull/343) and [#345](https://github.com/apify/apify-cli/pull/345)
- Better template language selection in `apify create` by [@mnmkng](https://github.com/mnmkng) in [#338](https://github.com/apify/apify-cli/pull/338)
- New documentation portal by [@barjin](https://github.com/barjin) in [#331](https://github.com/apify/apify-cli/pull/331)

#### Internal changes

- Added automated tests for Python support by [@fnesveda](https://github.com/fnesveda) in [#344](https://github.com/apify/apify-cli/pull/344)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.14.1...v0.15.0

## [v0.14.1](https://github.com/apify/apify-cli/releases/tag/v0.14.1)

#### What's Changed

- chore: Disable actor template prompt looping around by [@fnesveda](https://github.com/fnesveda) in [#318](https://github.com/apify/apify-cli/pull/318)
- feat: Support for running Python actors by [@fnesveda](https://github.com/fnesveda) in [#316](https://github.com/apify/apify-cli/pull/316)
- fix: Removing unneeded dependencies by [@mtrunkat](https://github.com/mtrunkat) in [#322](https://github.com/apify/apify-cli/pull/322)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.13.0...v0.14.1

## [v0.13.0](https://github.com/apify/apify-cli/releases/tag/v0.13.0)

#### What's Changed

- feat: Making outdated version warning more visible by [@mtrunkat](https://github.com/mtrunkat) in [#301](https://github.com/apify/apify-cli/pull/301)
- fix: fix headings in readme by [@mhamas](https://github.com/mhamas) in [#308](https://github.com/apify/apify-cli/pull/308)
- fix: Update node version by [@novotnyj](https://github.com/novotnyj) in [#314](https://github.com/apify/apify-cli/pull/314)
- fix: missing latest tag on first push by [@mnmkng](https://github.com/mnmkng) in [#312](https://github.com/apify/apify-cli/pull/312)

**Full Changelog**: https://github.com/apify/apify-cli/compare/v0.12.0...v0.13.0

## [v0.12.0](https://github.com/apify/apify-cli/releases/tag/v0.12.0)

- add the `X-Apify-Request-Origin: CLI` header to the API calls done by CLI

## [v0.11.1](https://github.com/apify/apify-cli/releases/tag/v0.11.1)

- Fix `create` command which rewrites `.actor/actor.json` from template with default file

## [v0.11.0](https://github.com/apify/apify-cli/releases/tag/v0.11.0)

- modify commands to work with actor config stored in `.actor/actor.json` instead of the deprecated `apify.json`
- add migration from the deprecated config to the new one
- modify `vis` and `edit-input-schema` commands to find the input schema at the correct location, where it would be loaded from on the platform
- update README and commands' help texts to cover these changes


================================================
File: /website/versioned_docs/version-0.20/reference.md
================================================
---
title: Command reference
---

This section contains printouts of `apify help` for all commands.

<!-- prettier-ignore-start -->
<!-- commands -->
* [`apify actor`](#apify-actor)
* [`apify actor get-input`](#apify-actor-get-input)
* [`apify actor get-value KEY`](#apify-actor-get-value-key)
* [`apify actor push-data [ITEM]`](#apify-actor-push-data-item)
* [`apify actor set-value KEY [VALUE]`](#apify-actor-set-value-key-value)
* [`apify call [ACTORID]`](#apify-call-actorid)
* [`apify create [ACTORNAME]`](#apify-create-actorname)
* [`apify help [COMMAND]`](#apify-help-command)
* [`apify info`](#apify-info)
* [`apify init [ACTORNAME]`](#apify-init-actorname)
* [`apify login`](#apify-login)
* [`apify logout`](#apify-logout)
* [`apify pull [ACTORID]`](#apify-pull-actorid)
* [`apify push [ACTORID]`](#apify-push-actorid)
* [`apify run`](#apify-run)
* [`apify secrets`](#apify-secrets)
* [`apify secrets add NAME VALUE`](#apify-secrets-add-name-value)
* [`apify secrets rm NAME`](#apify-secrets-rm-name)
* [`apify task`](#apify-task)
* [`apify task run TASKID`](#apify-task-run-taskid)
* [`apify validate-schema [PATH]`](#apify-validate-schema-path)

## `apify actor`

Commands are designed to be used in Actor runs. All commands are in PoC state, do not use in production environments.

```
USAGE
  $ apify actor

DESCRIPTION
  Commands are designed to be used in Actor runs. All commands are in PoC state, do not use in production environments.
```

_See code: [src/commands/actor/index.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/actor/index.ts)_

## `apify actor get-input`

Gets the Actor input value from the default key-value store associated with the Actor run.

```
USAGE
  $ apify actor get-input

DESCRIPTION
  Gets the Actor input value from the default key-value store associated with the Actor run.
```

_See code: [src/commands/actor/get-input.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/actor/get-input.ts)_

## `apify actor get-value KEY`

Gets a value from the default key-value store associated with the Actor run.

```
USAGE
  $ apify actor get-value KEY

ARGUMENTS
  KEY  Key of the record in key-value store

DESCRIPTION
  Gets a value from the default key-value store associated with the Actor run.
```

_See code: [src/commands/actor/get-value.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/actor/get-value.ts)_

## `apify actor push-data [ITEM]`

Stores an object or an array of objects to the default dataset of the Actor run.

```
USAGE
  $ apify actor push-data [ITEM]

ARGUMENTS
  ITEM  JSON string with one object or array of objects containing data to be stored in the default dataset.

DESCRIPTION
  Stores an object or an array of objects to the default dataset of the Actor run.
  It is possible to pass data using item argument or stdin.
  Passing data using argument:
  $ apify actor push-data {"foo": "bar"}
  Passing data using stdin with pipe:
  $ cat ./test.json | apify actor push-data
```

_See code: [src/commands/actor/push-data.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/actor/push-data.ts)_

## `apify actor set-value KEY [VALUE]`

Sets or removes record into the default KeyValueStore associated with the Actor run.

```
USAGE
  $ apify actor set-value KEY [VALUE] [-c <value>]

ARGUMENTS
  KEY    Key of the record in key-value store.
  VALUE  Record data, which can be one of the following values:
         - If empty, the record in the key-value store is deleted.
         - If no `contentType` flag is specified, value is expected to be any JSON string value.
         - If options.contentType is set, value is taken as is.

FLAGS
  -c, --contentType=<value>  Specifies a custom MIME content type of the record. By default "application/json" is used.

DESCRIPTION
  Sets or removes record into the default KeyValueStore associated with the Actor run.
  It is possible to pass data using argument or stdin.
  Passing data using argument:
  $ apify actor set-value KEY my-value
  Passing data using stdin with pipe:
  $ cat ./my-text-file.txt | apify actor set-value KEY --contentType text/plain
```

_See code: [src/commands/actor/set-value.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/actor/set-value.ts)_

## `apify call [ACTORID]`

Runs a specific Actor remotely on the Apify cloud platform.

```
USAGE
  $ apify call [ACTORID] [-b <value>] [-t <value>] [-m <value>] [-w <value>] [-i <value> | --input-file
    <value>] [-s] [-o]

ARGUMENTS
  ACTORID  Name or ID of the Actor to run (e.g. "my-actor", "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not
           provided, the command runs the remote Actor specified in the ".actor/actor.json" file.

FLAGS
  -b, --build=<value>            Tag or number of the build to run (e.g. "latest" or "1.2.34").
  -i, --input=<value>            Optional JSON input to be given to the Actor.
  -m, --memory=<value>           Amount of memory allocated for the Actor run, in megabytes.
  -o, --output-dataset           Prints out the entire default dataset on successful run of the Actor.
  -s, --silent                   Prevents printing the logs of the Actor run to the console.
  -t, --timeout=<value>          Timeout for the Actor run in seconds. Zero value means there is no timeout.
  -w, --wait-for-finish=<value>  Seconds for waiting to run to finish, if no value passed, it waits forever.
      --input-file=<value>       Optional path to a file with JSON input to be given to the Actor. The file must be a
                                 valid JSON file. You can also specify `-` to read from standard input.

DESCRIPTION
  Runs a specific Actor remotely on the Apify cloud platform.
  The Actor is run under your current Apify account. Therefore you need to be logged in by calling "apify login". It
  takes input for the Actor from the default local key-value store by default.
```

_See code: [src/commands/call.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/call.ts)_

## `apify create [ACTORNAME]`

Creates a new Actor project directory from a selected boilerplate template.

```
USAGE
  $ apify create [ACTORNAME] [-t <value>] [--skip-dependency-install] [--omit-optional-deps]

ARGUMENTS
  ACTORNAME  Name of the Actor and its directory

FLAGS
  -t, --template=<value>         Template for the Actor. If not provided, the command will prompt for it.
                                 Visit
                                 https://raw.githubusercontent.com/apify/actor-templates/master/templates/manifest.json
                                 to find available template names.
      --omit-optional-deps       Skip installing optional dependencies.
      --skip-dependency-install  Skip installing Actor dependencies.

DESCRIPTION
  Creates a new Actor project directory from a selected boilerplate template.
```

_See code: [src/commands/create.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/create.ts)_

## `apify help [COMMAND]`

Display help for apify.

```
USAGE
  $ apify help [COMMAND...] [-n]

ARGUMENTS
  COMMAND...  Command to show help for.

FLAGS
  -n, --nested-commands  Include all nested commands in the output.

DESCRIPTION
  Display help for apify.
```

_See code: [@oclif/plugin-help](https://github.com/oclif/plugin-help/blob/v6.2.10/src/commands/help.ts)_

## `apify info`

Displays information about the currently active Apify account.

```
USAGE
  $ apify info

DESCRIPTION
  Displays information about the currently active Apify account.
  The information is printed to the console.
```

_See code: [src/commands/info.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/info.ts)_

## `apify init [ACTORNAME]`

Initializes a new Actor project in an existing directory.

```
USAGE
  $ apify init [ACTORNAME] [-y]

ARGUMENTS
  ACTORNAME  Name of the Actor. If not provided, you will be prompted for it.

FLAGS
  -y, --yes  Automatic yes to prompts; assume "yes" as answer to all prompts. Note that in some cases, the command may
             still ask for confirmation.

DESCRIPTION
  Initializes a new Actor project in an existing directory.
  If the directory contains a Scrapy project in Python, the command automatically creates wrappers so that you can run
  your scrapers without changes.

  The command creates the ".actor/actor.json" file and the "storage" directory in the current directory, but does not
  touch any other existing files or directories.

  WARNING: The directory at "storage" will be overwritten if it already exists.
```

_See code: [src/commands/init.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/init.ts)_

## `apify login`

Logs in to your Apify account.

```
USAGE
  $ apify login [-t <value>] [-m console|manual]

FLAGS
  -m, --method=<option>  [Optional] Method of logging in to Apify
                         <options: console|manual>
  -t, --token=<value>    [Optional] Apify API token

DESCRIPTION
  Logs in to your Apify account.
  The API token and other account information is stored in the ~/.apify directory, from where it is read by all other
  "apify" commands. To log out, call "apify logout".
```

_See code: [src/commands/login.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/login.ts)_

## `apify logout`

Logs out of your Apify account.

```
USAGE
  $ apify logout

DESCRIPTION
  Logs out of your Apify account.
  The command deletes the API token and all other account information stored in the ~/.apify directory. To log in again,
  call "apify login".
```

_See code: [src/commands/logout.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/logout.ts)_

## `apify pull [ACTORID]`

Pulls an Actor from the Apify platform to the current directory. If it is defined as Git repository, it will be cloned. If it is defined as Web IDE, it will fetch the files.

```
USAGE
  $ apify pull [ACTORID] [-v <value>]

ARGUMENTS
  ACTORID  Name or ID of the Actor to run (e.g. "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not provided, the
           command will update the Actor in the current directory based on its name in ".actor/actor.json" file.

FLAGS
  -v, --version=<value>  Actor version number which will be pulled, e.g. 1.2. Default: the highest version

DESCRIPTION
  Pulls an Actor from the Apify platform to the current directory. If it is defined as Git repository, it will be
  cloned. If it is defined as Web IDE, it will fetch the files.
```

_See code: [src/commands/pull.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/pull.ts)_

## `apify push [ACTORID]`

Uploads the Actor to the Apify platform and builds it there.

```
USAGE
  $ apify push [ACTORID] [--version-number <value>] [-v <value>] [-b <value>] [-w <value>] [--no-prompt]
    [--force]

ARGUMENTS
  ACTORID  Name or ID of the Actor to push (e.g. "apify/hello-world" or "E2jjCZBezvAZnX8Rb"). If not provided, the
           command will create or modify the Actor with the name specified in ".actor/actor.json" file.

FLAGS
  -b, --build-tag=<value>        Build tag to be applied to the successful Actor build. By default, it is taken from the
                                 ".actor/actor.json" file
  -v, --version=<value>          Actor version number to which the files should be pushed. By default, it is taken from
                                 the ".actor/actor.json" file.
  -w, --wait-for-finish=<value>  Seconds for waiting to build to finish, if no value passed, it waits forever.
      --force                    Push an Actor even when the local files are older than the Actor on the platform.
      --no-prompt                Do not prompt for opening the Actor details in a browser. This will also not open the
                                 browser automatically.
      --version-number=<value>   DEPRECATED: Use flag version instead. Actor version number to which the files should be
                                 pushed. By default, it is taken from the ".actor/actor.json" file.

DESCRIPTION
  Uploads the Actor to the Apify platform and builds it there.
  The Actor settings are read from the ".actor/actor.json" file in the current directory, but they can be overridden
  using command-line options.
  NOTE: If the source files are smaller than 3 MB then they are uploaded as
  "Multiple source files", otherwise they are uploaded as "Zip file".

  When there's an attempt to push files that are older than the Actor on the platform, the command will fail. Can be
  overwritten with --force flag.
```

_See code: [src/commands/push.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/push.ts)_

## `apify run`

Runs the Actor locally in the current directory.

```
USAGE
  $ apify run [-p] [--purge-queue] [--purge-dataset] [--purge-key-value-store] [--entrypoint <value>] [-i
    <value> | --input-file <value>]

FLAGS
  -i, --input=<value>          Optional JSON input to be given to the Actor.
  -p, --purge                  Shortcut that combines the --purge-queue, --purge-dataset and --purge-key-value-store
                               options.
      --entrypoint=<value>     Optional entrypoint for running with injected environment variables.
                               For Python, it is the module name, or a path to a file.
                               For node.js, it is the npm script name, or a path to a JS/MJS file. You can also pass in
                               a directory name, provided that directory contains an "index.js" file.
      --input-file=<value>     Optional path to a file with JSON input to be given to the Actor. The file must be a
                               valid JSON file. You can also specify `-` to read from standard input.
      --purge-dataset          Deletes the local directory containing the default dataset before the run starts.
      --purge-key-value-store  Deletes all records from the default key-value store in the local directory before the
                               run starts, except for the "INPUT" key.
      --purge-queue            Deletes the local directory containing the default request queue before the run starts.

DESCRIPTION
  Runs the Actor locally in the current directory.
  It sets various APIFY_XYZ environment variables in order to provide a working execution environment for the Actor. For
  example, this causes the Actor input, as well as all other data in key-value stores, datasets or request queues to be
  stored in the "storage" directory, rather than on the Apify platform.

  NOTE: You can override the command's default behavior for Node.js Actors by overriding the "start" script in the
  package.json file. You can set up your own main file or environment variables by changing it.
```

_See code: [src/commands/run.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/run.ts)_

## `apify secrets`

Manages secret values for Actor environment variables.

```
USAGE
  $ apify secrets

DESCRIPTION
  Manages secret values for Actor environment variables.

  Example:
  $ apify secrets add mySecret TopSecretValue123

  Now the "mySecret" value can be used in an environment variable defined in ".actor/actor.json" file by adding the "@"
  prefix:

  {
  "actorSpecification": 1,
  "name": "my_actor",
  "environmentVariables": { "SECRET_ENV_VAR": "@mySecret" },
  "version": "0.1
  }

  When the Actor is pushed to Apify cloud, the "SECRET_ENV_VAR" and its value is stored as a secret environment variable
  of the Actor.
```

_See code: [src/commands/secrets/index.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/secrets/index.ts)_

## `apify secrets add NAME VALUE`

Adds a new secret value.

```
USAGE
  $ apify secrets add NAME VALUE

ARGUMENTS
  NAME   Name of the secret
  VALUE  Value of the secret

DESCRIPTION
  Adds a new secret value.
  The secrets are stored to a file at ~/.apify
```

_See code: [src/commands/secrets/add.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/secrets/add.ts)_

## `apify secrets rm NAME`

Removes the secret.

```
USAGE
  $ apify secrets rm NAME

ARGUMENTS
  NAME  Name of the secret

DESCRIPTION
  Removes the secret.
```

_See code: [src/commands/secrets/rm.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/secrets/rm.ts)_

## `apify task`

Commands are designed to be used to interact with Tasks.

```
USAGE
  $ apify task

DESCRIPTION
  Commands are designed to be used to interact with Tasks.
```

_See code: [src/commands/task/index.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/task/index.ts)_

## `apify task run TASKID`

Runs a specific Actor remotely on the Apify cloud platform.

```
USAGE
  $ apify task run TASKID [-b <value>] [-t <value>] [-m <value>] [-w <value>]

ARGUMENTS
  TASKID  Name or ID of the Task to run (e.g. "my-task" or "E2jjCZBezvAZnX8Rb").

FLAGS
  -b, --build=<value>            Tag or number of the build to run (e.g. "latest" or "1.2.34").
  -m, --memory=<value>           Amount of memory allocated for the Task run, in megabytes.
  -t, --timeout=<value>          Timeout for the Task run in seconds. Zero value means there is no timeout.
  -w, --wait-for-finish=<value>  Seconds for waiting to run to finish, if no value passed, it waits forever.

DESCRIPTION
  Runs a specific Actor remotely on the Apify cloud platform.
  The Actor is run under your current Apify account. Therefore you need to be logged in by calling "apify login". It
  takes input for the Actor from the default local key-value store by default.
```

_See code: [src/commands/task/run.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/task/run.ts)_

## `apify validate-schema [PATH]`

Validates input schema and prints errors found.

```
USAGE
  $ apify validate-schema [PATH]

ARGUMENTS
  PATH  Optional path to your INPUT_SCHEMA.json file. If not provided ./INPUT_SCHEMA.json is used.

DESCRIPTION
  Validates input schema and prints errors found.
  The input schema for the Actor is used from these locations in order of preference.
  The first one found is validated as it would be the one used on the Apify platform.
  1. Directly embedded object in ".actor/actor.json" under 'input' key
  2. Path to JSON file referenced in ".actor/actor.json" under 'input' key
  3. JSON file at .actor/INPUT_SCHEMA.json
  4. JSON file at INPUT_SCHEMA.json

  You can also pass any custom path to your input schema to have it validated instead.
```

_See code: [src/commands/validate-schema.ts](https://github.com/apify/apify-cli/blob/v0.20.10/src/commands/validate-schema.ts)_
<!-- commandsstop -->
<!-- prettier-ignore-end -->


================================================
File: /website/versioned_docs/version-0.20/telemetry.md
================================================
---
sidebar_label: Telemetry
title: Telemetry
---

Apify collects telemetry data about the general usage of the CLI to help us improve the product. Participation in this program is optional and you may opt out if you prefer not to share any information.

## Data Collection

All telemetry data is collected and stored securely on [Mixpanel](https://mixpanel.com/). We do not collect any sensitive information such as your API token or personal information.

### Metrics Collected

Before a user connects to the Apify platform, we collect anonymous information about CLI usage including:

- Usage of all commands
- Internal attributes of the local environment (OS, shell, Node.js version, Python version, Apify CLI version)
- For the `actor create` command, we identify which template was used to create the Actor (language, template name, template ID)

After a user connects to the Apify platform (successful `apify login`), we collect the same information about CLI usage along with the ID of the connected user. You can read more about how we protect personal information in our [Privacy Policy](https://apify.com/privacy-policy).

## How to opt out

You can disable telemetry by setting the "APIFY_CLI_DISABLE_TELEMETRY" environment variable to "1". After setting this variable, the CLI will not send any telemetry data whether you are connected with Apify or not.


================================================
File: /website/versioned_docs/version-0.20/index.md
================================================
---
title: Apify CLI
---

<a href="https://www.npmjs.com/package/apify-cli"><img src="https://badge.fury.io/js/apify-cli.svg" alt="npm version" loading="lazy" /></a>
<a href="https://travis-ci.com/apify/apify-cli?branch=master"><img src="https://travis-ci.com/apify/apify-cli.svg?branch=master" loading="lazy" alt="Build Status" /></a>

Apify command-line interface (Apify CLI) helps you create, develop, build and run
[Apify Actors](https://apify.com/actors),
and manage the Apify cloud platform from any computer.

Apify Actors are cloud programs that can perform arbitrary web scraping, automation or data processing job.
They accept input, perform their job and generate output.
While you can develop Actors in an online IDE directly in the [Apify web application](https://console.apify.com/),
for complex projects it is more convenient to develop Actors locally on your computer
using <a href="https://github.com/apify/apify-sdk-js">Apify SDK</a>
and only push the Actors to the Apify cloud during deployment.
This is where the Apify CLI comes in.

Note that Actors running on the Apify platform are executed in Docker containers, so with an appropriate `Dockerfile`
you can build your Actors in any programming language.
However, we recommend using JavaScript / Node.js, for which we provide most libraries and support.


================================================
File: /website/versioned_docs/version-0.20/installation.md
================================================
---
title: Installation
description: Learn how to install Apify CLI, and how to create, run, and manage Actors through it.
sidebar_label: Installation
---

## Installation

You can install Apify CLI either using [Homebrew package manager](https://brew.sh) on macOS or Linux or using NPM on all platforms including Windows.

### Via Homebrew

Run the following command:

```bash showLineNumbers
brew install apify-cli
```

### Via NPM

First, make sure you have [Node.js](https://nodejs.org) version 18 or higher with NPM installed on your computer:

```bash showLineNumbers
node --version
npm --version
```

Install or upgrade Apify CLI by running:

```bash showLineNumbers
npm -g install apify-cli
```

If you receive a permission error, read npm's [official guide](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally) on installing packages globally.

Alternatively, you can use [Node Version Manager (nvm)](https://github.com/nvm-sh/nvm) and install Apify CLI only into a selected user-level Node version without requiring root privileges:

```bash showLineNumbers
nvm install 18
nvm use 18
npm -g install apify-cli
```

After using either of these methods , verify that Apify CLI was installed correctly by running:

```bash showLineNumbers
apify --version
```

which should print something like:

```bash showLineNumbers
apify-cli/0.19.1 linux-x64 node-v18.17.0
```

## Basic Usage

The following examples demonstrate the basic usage of Apify CLI.

### Create a New Actor from Scratch

```bash showLineNumbers
apify create my-hello-world
```

First, you will be prompted to select a template with the boilerplate for the Actor, to help you get started quickly.
The command will create a directory called `my-hello-world` that contains a Node.js project
for the Actor and a few configuration files.

### Create a New Actor from Existing Project

:::tip Automatic Actor directory initialization
When you create an Actor using the `apify create` command, the directory will already be initialized.
:::

```bash showLineNumbers
cd ./my/awesome/project
apify init
```

This command will only set up local Actor development environment in an existing directory,
i.e. it will create the `.actor/actor.json` file and `apify_storage` directory.

Before you can run your project locally using `apify run`, you have to set up the right start command in `package.json` under scripts.start. For example:

```json showLineNumbers
{
    ...
    "scripts": {
        "start": "node your_main_file.js",
    },
    ...
}
```

You can find more information about by running `apify help run`.

### Run the Actor Locally

```bash showLineNumbers
cd my-hello-world
apify run
```

This command runs the Actor on your local machine.
Now's your chance to develop the logic - or magic :smirk:

### Login with your Apify account

```bash showLineNumbers
apify login
```

Before you can interact with the Apify cloud, you need to [create an Apify account](https://console.apify.com/)
and log in to it using the above command. You will be prompted for
your [Apify API token](https://console.apify.com/settings/integrations).

:::note API token save directory
The command will store the API token and other sensitive information to `~/.apify`.
:::

### Push t
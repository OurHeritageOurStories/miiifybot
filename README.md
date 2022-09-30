# Miiifybot

## Introduction

Miiifybot is a Discord chatbot for integration into Mozilla Hubs. It builds on technology available in [Miiify](https://github.com/nationalarchives/miiify) to allow the community to interact with content displayed in a 3D virtual gallery. Users can learn about the content on display and also contribute back their knowledge. All contributions go through a review process before being accessible within the platform or within IIIF viewers.

## Chatbot commands

To display all annotations associated with the item:
```
$about <item>
```

To create a new annotation for an item. This will then be submitted for review before being accessible to all.
```
$describe <item> <description>
```

## Discord channel

The channel is available via the following invite link:
```
https://discord.gg/QmHfjAtBDp
```

## Example gallery

You can try an example gallery of cats from Wikidata:

https://hubs.mozilla.com/dcRzw4T/general

The annotations are available in standard IIIF viewers:

https://projectmirador.org/embed/?iiif-content=https://miiifystore.s3.eu-west-2.amazonaws.com/iiif/manifest.json


The data is also accessible from the annotation server:


https://miiify.rocks/annotations/cats


You can even access the data directly in its GitHub repository:

https://github.com/jptmoore/annotations/tree/master/cats/collection

## Tutorial

To find out what contributions have been made to the cat with label p1 we would do the following:
```
$about p1
```

To make a new contribution we could do the following:
```
$describe p1 this is a cute cat!
```
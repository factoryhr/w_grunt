w_grunt - sublime plugin
=======

<h3>Usage</h3>
To use plugin create grunt file, or copy the Gruntfile.js from this repository and configure it. To learn more about grunt wisit http://gruntjs.com/
<br>
<br>

Create w_grunt.json file. This is configuration file for plugin.<br>
You must specify all of the keys from example below.

```
{
	"grunt_on_save": true,

	"copy_to_clipboard" : true,
	"copy_dev_source" : false,

	"devSource" : "build/dev/build.js",
	"productSource" : "build/production/build.min.js"
}
```

``` copy_to_clipboard ``` - If true it will copy the generated dev or production source<br>
``` copy_dev_source ``` - If true it will copy dev source to clipboard, false - production source<br>
``` devSource ``` - Destination of development sources<br>
``` productSource ``` - Destionation of production sources<br>

Note ``` devSource ``` and ``` productSource ``` must be the configured inside Gruntfile.js. You can load w_grunt.json file and use information from it.





module.exports = function(grunt) {

    var ops = grunt.file.readJSON("w_grunt.json");

    var tasks = {
        pkg: grunt.file.readJSON('package.json'),

        concat:{
            options: {
                separator: ';',
            },
            dist: {
                src: ['src/**/*.js'],
                dest: ops.devSource,
            }
        },

        uglify: {
            options: {
                mangle: false
            },
            my_target: {
                files: {
                    
                }
            }
        }
    }

    tasks["uglify"]["my_target"]["files"][ops.productSource] = ops.devSource;

    grunt.initConfig(tasks);
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.registerTask('default', ["concat", "uglify"]);
};













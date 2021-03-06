module.exports = function(grunt) {
    grunt.initConfig({
        browserify: {
            standalone: {
                src: ['js/main.js'],
                dest: 'js/bundle.js'
            }
        },

        cssmin: {
            minify: {
                src: 'css/style.css',
                dest: 'css/style.min.css'
            }
        },

        less: {
            development: {
                options: {
                    paths: ["css"],
                    yuicompress: true
                },
                files: {
                    "css/style.css": "css/style.less"
                }
            }
        },

        watch: {
            browserify: {
                files: [],
                tasks: ["browserify"]
            },

            less: {
                files: ["css/*.less", "css/*/*.less"],
                tasks: ["less", "cssmin"]
            }

        }
    });

    grunt.loadNpmTasks('grunt-browserify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');
};

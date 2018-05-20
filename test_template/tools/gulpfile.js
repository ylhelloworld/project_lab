var gulp = require('gulp');
var concat = require('gulp-concat')
var sass =require("gulp-sass")
 
gulp.task('default',['concat_vendors_js',
                    'concat_vendors_css',
                    "concat_vendors_media",
                    "concat_vendors_fonts",
                    "concat_default_js",
                    "scss_default",
                    "concat_default_media"
                ]);

                
gulp.task("concat_vendors_js",function(){ 
    gulp.src([
        "node_modules/jquery/dist/jquery.js",
        "node_modules/popper.js/dist/umd/popper.js",
        "node_modules/bootstrap/dist/js/bootstrap.min.js",
        "node_modules/js-cookie/src/js.cookie.js",
        "node_modules/jquery-smooth-scroll/jquery.smooth-scroll.js",
        "node_modules/moment/min/moment.min.js",
        "node_modules/wnumb/wNumb.js",
        "node_modules/jquery.repeater/src/intro.js",
        "node_modules/jquery.repeater/src/lib.js",
        "node_modules/jquery.repeater/src/jquery.input.js",
        "node_modules/jquery.repeater/src/repeater.js",
        "node_modules/jquery.repeater/src/outro.js",
        "node_modules/jquery-form/dist/jquery.form.min.js",
        "node_modules/malihu-custom-scrollbar-plugin/jquery.mCustomScrollbar.js",
        "node_modules/block-ui/jquery.blockUI.js",
        "node_modules/bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js",
        "node_modules/bootstrap-datetime-picker/js/bootstrap-datetimepicker.min.js",
        "node_modules/bootstrap-timepicker/js/bootstrap-timepicker.min.js",
        "../src/js/framework/components/plugins/forms/bootstrap-timepicker.init.js",
        "node_modules/bootstrap-daterangepicker/daterangepicker.js",
        "../src/js/framework/components/plugins/forms/bootstrap-daterangepicker.init.js",
        "node_modules/bootstrap-touchspin/dist/jquery.bootstrap-touchspin.js",
        "node_modules/bootstrap-maxlength/src/bootstrap-maxlength.js",
        "node_modules/bootstrap-switch/dist/js/bootstrap-switch.js",
        "../src/js/framework/components/plugins/forms/bootstrap-switch.init.js",
        "../src/vendors/bootstrap-multiselectsplitter/bootstrap-multiselectsplitter.min.js",
        "node_modules/bootstrap-select/dist/js/bootstrap-select.js",
        "node_modules/select2/dist/js/select2.js",
        "node_modules/typeahead.js/dist/typeahead.bundle.js",
        "node_modules/handlebars/dist/handlebars.js",
        "node_modules/inputmask/dist/jquery.inputmask.bundle.js",
        "node_modules/inputmask/dist/inputmask/inputmask.date.extensions.js",
        "node_modules/inputmask/dist/inputmask/inputmask.numeric.extensions.js",
        "node_modules/inputmask/dist/inputmask/inputmask.phone.extensions.js",
        "node_modules/nouislider/distribute/nouislider.js",
        "node_modules/autosize/dist/autosize.js",
        "node_modules/clipboard/dist/clipboard.min.js",
        "node_modules/ion-rangeslider/js/ion.rangeSlider.js",
        "node_modules/dropzone/dist/dropzone.js",
        "node_modules/summernote/dist/summernote.js",
        "node_modules/markdown/lib/markdown.js",
        "node_modules/bootstrap-markdown/js/bootstrap-markdown.js",
        "../src/js/framework/components/plugins/forms/bootstrap-markdown.init.js",
        "node_modules/jquery-validation/dist/jquery.validate.js",
        "node_modules/jquery-validation/dist/additional-methods.js",
        "../src/js/framework/components/plugins/forms/jquery-validation.init.js",
        "node_modules/bootstrap-notify/bootstrap-notify.min.js",
        "../src/js/framework/components/plugins/base/bootstrap-notify.init.js",
        "node_modules/toastr/build/toastr.min.js",
        "node_modules/jstree/dist/jstree.js",
        "node_modules/raphael/raphael.js",
        "node_modules/morris.js/morris.js",
        "node_modules/chartist/dist/chartist.js",
        "node_modules/chart.js/dist/Chart.bundle.js",
        "../src/js/framework/components/plugins/charts/chart.init.js",
        "../src/vendors/bootstrap-session-timeout/dist/bootstrap-session-timeout.min.js",
        "../src/vendors/jquery-idletimer/idle-timer.min.js",
        "node_modules/waypoints/lib/jquery.waypoints.js",
        "node_modules/counterup/jquery.counterup.js",
        "node_modules/es6-promise-polyfill/promise.min.js",
        "node_modules/sweetalert2/dist/sweetalert2.min.js",               
        "../src/js/framework/components/plugins/base/sweetalert2.init.js",
        "../src/vendors/jquery-ui/jquery-ui.min.js",
        "node_modules/fullcalendar/dist/fullcalendar.js",
        "node_modules/fullcalendar/dist/gcal.js",
        "node_modules/gmaps/gmaps.js",
        "node_modules/jqvmap/dist/jquery.vmap.js",
        "node_modules/jqvmap/dist/maps/jquery.vmap.europe.js",
        "node_modules/jqvmap/dist/maps/jquery.vmap.germany.js",
        "node_modules/jqvmap/dist/maps/jquery.vmap.russia.js",
        "node_modules/jqvmap/dist/maps/jquery.vmap.usa.js",
        "node_modules/jqvmap/dist/maps/jquery.vmap.world.js",
        "node_modules/jquery-flot/jquery.flot.js",
        "node_modules/jquery-flot/jquery.flot.resize.js",
        "node_modules/jquery-flot/jquery.flot.categories.js",
        "node_modules/jquery-flot/jquery.flot.pie.js",
        "node_modules/jquery-flot/jquery.flot.stack.js",
        "node_modules/jquery-flot/jquery.flot.crosshair.js",
        "node_modules/jquery-flot/jquery.flot.axislabels.js"  
    ]) .pipe(concat('vendors.bundle.js')).pipe(gulp.dest('../dist/assets/vendors/js'));
})
gulp.task("concat_vendors_css",function(){ 
    gulp.src([
        "node_modules/tether/dist/css/tether.css",
        "node_modules/malihu-custom-scrollbar-plugin/jquery.mCustomScrollbar.css",
        "node_modules/bootstrap-datepicker/dist/css/bootstrap-datepicker3.min.css",
        "node_modules/bootstrap-datetime-picker/css/bootstrap-datetimepicker.min.css",
        "node_modules/bootstrap-timepicker/css/bootstrap-timepicker.min.css",
        "node_modules/bootstrap-daterangepicker/daterangepicker.css",
        "node_modules/bootstrap-touchspin/dist/jquery.bootstrap-touchspin.css",
        "node_modules/bootstrap-switch/dist/css/bootstrap3/bootstrap-switch.css",
        "node_modules/bootstrap-select/dist/css/bootstrap-select.css",
        "node_modules/select2/dist/css/select2.css",
        "node_modules/nouislider/distribute/nouislider.css",
        "node_modules/ion-rangeslider/css/ion.rangeSlider.css",
        "node_modules/ion-rangeslider/css/ion.rangeSlider.skinFlat.css",
        "node_modules/dropzone/dist/dropzone.css",
        "node_modules/summernote/dist/summernote.css",
        "node_modules/bootstrap-markdown/css/bootstrap-markdown.min.css",
        "node_modules/animate.css/animate.min.css",
        "node_modules/toastr/build/toastr.css",
        "node_modules/jstree/dist/themes/default/style.css",
        "node_modules/morris.js/morris.css",
        "node_modules/chartist/dist/chartist.css",
        "node_modules/socicon/css/socicon.css",
        "node_modules/font-awesome/css/font-awesome.css",
        "../src/vendors/line-awesome/css/line-awesome.css",
        "../src/vendors/flaticon/css/flaticon.css",
        "../src/vendors/metronic/css/styles.css",
        "node_modules/sweetalert2/dist/sweetalert2.min.css",
        "../src/vendors/jquery-ui/jquery-ui.min.css",
        "node_modules/fullcalendar/dist/fullcalendar.css",
        "node_modules/jqvmap/dist/jqvmap.css"
    ]) .pipe(concat('vendors.bundle.css')).pipe(gulp.dest('../dist/assets/vendors/css'));
})

gulp.task("concat_vendors_media",function(){ 
    gulp.src([
        "node_modules/malihu-custom-scrollbar-plugin/mCSB_buttons.png" ]) .pipe(gulp.dest('../dist/assets/vendors/images/malihu-custom-scrollbar-plugin'));
    gulp.src([  "node_modules/ion-rangeslider/img/sprite-skin-flat.png" ]) .pipe(gulp.dest('../dist/assets/vendors/images/ion-rangeslider'));
    gulp.src([ 
        "../src/vendors/jstree/32px.png",
        "node_modules/jstree/dist/themes/default/40px.png",
        "node_modules/jstree/dist/themes/default/*.gif"
    ]) .pipe(gulp.dest('../dist/assets/vendors/images/jstree'));
})
 
gulp.task("concat_vendors_fonts",function(){ 
    gulp.src(["node_modules/summernote/dist/font/**" ,
                "node_modules/socicon/font/**",
                "node_modules/font-awesome/fonts/**",
                "../src/vendors/flaticon/fonts/**",
                "../src/vendors/line-awesome/fonts/**" ,
                "../src/vendors/metronic/fonts/**" 
            ]) .pipe(gulp.dest('../dist/assets/vendors/fonts'));
    // gulp.src(["node_modules/summernote/dist/font/**" ]) .pipe(gulp.dest('../dist/assets/vendors/fonts/summernote'));
    // gulp.src([ "node_modules/socicon/font/**" ]) .pipe(gulp.dest('../dist/assets/vendors/fonts/socicon'));
    // gulp.src([ "node_modules/font-awesome/fonts/**"  ]) .pipe(gulp.dest('../dist/assets/vendors/fonts/font-awesome'));
    // gulp.src([ "../src/vendors/flaticon/fonts/**" ]) .pipe(gulp.dest('../dist/assets/vendors/fonts/flaticon'));
    // gulp.src([  "../src/vendors/line-awesome/fonts/**" ]) .pipe(gulp.dest('../dist/assets/vendors/fonts/line-awesome'));
    // gulp.src([ "../src/vendors/metronic/fonts/**" ]) .pipe(gulp.dest('../dist/assets/vendors/fonts/metronic'));
})


gulp.task("concat_default_js",function(){ 
    gulp.src([
        "../src/js/framework/base/**/*.js",
        "../src/js/framework/components/general/datatable/datatable.js",
        "../src/js/framework/**/*.js",
        "../src/js/demo/default/base/**/*.js",
        "../src/js/app/base/**/*.js",
        "../src/js/snippets/base/**/*.js",
        "../src/js/demo/default/custom/**/*.js"
        
    ]) .pipe(concat('scripts.bundle.js')).pipe(gulp.dest('../dist/assets/default/js'));
})

gulp.task("scss_default",function(){ 
    gulp.src([ "../src/sass/demo/default/style.scss"]) .pipe(sass({
        errLogToConsole: true,
        includePaths: ['../src/sass/framework', '../src/sass/framework/vendors/bootstrap'],
      })).pipe(gulp.dest('../dist/assets/default/css'));
})

gulp.task("concat_default_media",function(){ 
    gulp.src(["../src/media/demo/default/**/*.*"]) .pipe(gulp.dest('../dist/assets/default/media'));
    gulp.src(["../src/media/app/**/*.*"]) .pipe(gulp.dest('../dist/assets/default/media/app'));
})


 


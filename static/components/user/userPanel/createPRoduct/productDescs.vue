<template>
  <div id="productDescs" class="productSection">
    <div id="productDescsWrapper">
      <label for='tinymce'>توضیحات محصول را بنویسید</label>
      <br/>

      <textarea name='descs'>Welcome to TinyMCE!</textarea>
    </div>
  </div>
</template>

<script>
export default {
    mounted(){
                tinymce.init({
                    selector: 'textarea',
                    plugins: 'advlist autolink lists link image charmap print preview hr anchor pagebreak',
                    toolbar_mode: 'floating',
                    menubars:false,
                    width:'100%',
                    padding:'5px',
                    directionality : 'rtl',
                    textcolor_cols: "5",
                    toolbar:"image| forecolor backcolor | undo redo | styleselect | numlist bullist | bold italic | alignleft aligncenter alignright alignjustify | outdent indent",
                    // toolbar1:"image",
                    language:'fa',
                    image_title:true,
                    automatic_uploads:true,
                    file_picker_types:"image",
                    images_upload_base_path: '/some/basepath',
                    file_picker_callback: function(cb, value, meta) {
                        var input = document.createElement('input');
                        input.setAttribute('type', 'file');
                        input.setAttribute('accept', 'image/*');
                        input.onchange = function() {
                        var file = this.files[0];
                        var reader = new FileReader();
                        reader.onload = function () {
                            var id = 'blobid' + (new Date()).getTime();
                            var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
                            var base64 = reader.result.split(',')[1];
                            var blobInfo = blobCache.create(id, file, base64);
                            blobCache.add(blobInfo);
                            cb(blobInfo.blobUri(), { title: file.name });
                        };
                        reader.readAsDataURL(file);
                        }
                            input.click();

                    },
                    init_instance_callback : function(editor) {
                        var freeTiny = document.querySelector('.tox-notifications-container');
                        const brand=document.querySelector(".tox-statusbar__branding")
                        brand.style.display='none'
                        freeTiny.style.display = 'none';
                    }
                });
    }
}
</script>

<style scoped>
    
    label{
            color:#0061af;
            font-size:17pt;
            font-weight: lighter;
    }
    #productDescsWrapper{
        padding:10px;
        width:100%;
        display:flex;
        flex-direction:column;
        align-items:flex-end
    }
    #productDescs textarea{
        width:100%;
        height:500px;
        padding:5px;
    }
</style>
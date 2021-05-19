const uploadForm = document.getElementById('upload-form')
console.log(uploadForm)
const uploadDoc = document.getElementById('upload-document')
console.log(uploadDoc)
const submitbtn = document.getElementById('submit')
const progressBox = document.getElementById('progress-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')
console.log(csrf)

uploadDoc.addEventListener('change', ()=>{
    progressBox.classList.remove('not-visible')
    cancelBox.classList.remove('not-visible')
    $.ajax({
        type:'POST',
        url: uploadForm.action,
        enctype: 'multipart/form-data',
        data: fd,
        beforeSend: function(){
            console.log('before')
        },
        xhr: function(){
            const xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener('progress', e=>{
                console.log(e)
                if (e.lengthComputable) {
                    const percent = e.loaded / e.total * 100
                    console.log(percent)
                    progressBox.innerHTML = `<div class="progress">
                                                <div class="progress-bar" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                            <p>${percent.toFixed(1)}%</p>`
                }
            })}})})

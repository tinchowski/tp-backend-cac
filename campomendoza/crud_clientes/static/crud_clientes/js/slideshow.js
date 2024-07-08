function moveLeft(event){
    const container=event.target.parentNode
    const images=container.getElementsByTagName('img')
    let pos=0
    for(let i=0;i<images.length;i++){
        const style=window.getComputedStyle(images[i])
        if(style.display === 'block'){
            pos=i
            break
        }
    }
    images[pos].style.display='none'
    let prev=pos-1
    if(prev<0){
        prev=images.length-1
    }
    images[prev].style.display='block'
}   
function moveRight(event){
    const container=event.target.parentNode
    const images=container.getElementsByTagName('img')
    let pos=0
    for(let i=0;i<images.length;i++){
        const style=window.getComputedStyle(images[i])
        if(style.display === 'block'){
            pos=i
            break
        }
    }
    images[pos].style.display='none'
    let next=pos+1
    if(next>=images.length){
        next=0
    }
    images[next].style.display='block'
}   

document.querySelectorAll('.w3-button.w3-display-left')
    .forEach((el)=>{el.onclick=moveLeft})

document.querySelectorAll('.w3-button.w3-display-right')
    .forEach((el)=>{el.onclick=moveRight})

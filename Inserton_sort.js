// inserton sort by js
var arr =[1,3,4,2,5,6,9,8,7]
function Inserton_sort(arr){
    for(var i = 1;i < arr.length;i++){
        var item =arr[i]
        var j = i-1
        while(j >= 0 && arr[j]> item){
            arr[j+1] = arr[j]
            j-=1
        }
        arr[j+1] = item
    }
    return arr
}
console.log(Inserton_sort(arr))
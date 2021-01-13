// binary search by javascript
var list =[1,2,4,5,6,7,8,9,11,13,15,25,36]
var value = 2
function MyFunction(list,value){
    var left =0
    var right = list.length
    while(left <= right){
        var f_div = (left+right)/2
        var mid  = Math.floor(f_div)
        if(list[mid]== value){
            return mid
        }else if(list[mid] < value){
            left = mid + 1
        }else{
            right = mid - 1
        }
    }
    return -1
}
console.log(MyFunction(list,value))
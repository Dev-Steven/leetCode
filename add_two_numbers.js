/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var l1Num = toNumber(l1);
    console.log("first number: ", l1Num)
    var l2Num = toNumber(l2);
    console.log("second number: ", l2Num)
    
    var total = l1Num + l2Num;
    console.log("total: ", total)
    
    // convert to array
    var arr = toArray(total);
    
    var l3 = new ListNode(arr[arr.length-1]);
    console.log("l3: ", l3);
    var current = l3;
    
    for(var i = arr.length-2; i>=0; i--) {

        while(current.next !== null){
            current = current.next;
        }
        current.next = new ListNode(arr[i]);

        console.log("i: ", arr[i])
        console.log("l3: ", l3)
    }
    console.log("l3: ", l3)
    return l3;
    
};

function toNumber(linkedList) {
    // create an empty arraylist
    var numList = [];
    // empty string
    var linkedString = "";
    
    // obtain linked list
    let current = linkedList;
    
    // iterate and push into array
    while(current != null) {
        numList.push(current.val);
        current = current.next;
    }
    
    // take array and concatenate to string
    for(var i=numList.length-1; i>=0; i--) {
        linkedString = linkedString + numList[i];
    }
    
    // converting string to number
    var num = parseInt(linkedString, 10);
    
    return num
}

function toArray(num) {
    var arr = [];
    var string = num.toString();
    var length = string.length;
    
    for(var i=0; i<length; i++){
        arr.push(string[i]);
    }
    
    return arr;
}

function add(linkedList, arr) {
    var current = linkedList;
    while(current.next !== null){
        current = current.next;
    }
    current.next = arr;
    for(var i = arr[arr.length-2]; i>=0; i--) {
        linkedList.next = arr[i]
        
    }
    
}

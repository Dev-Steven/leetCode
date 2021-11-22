// O(n^2) time | O(1) space
function longestPalindrome(s: string): string {
	let result = '';
	let resultLength = 0;

	for (let index = 0; index < s.length; index++) {
		// even cases
		let left = index;
		let right = index;
		while (left >= 0 && right < s.length && s[left] === s[right]) {
			let checked = checkSubstring(left, right, result, resultLength, s);
			[result, resultLength] = checked;
			left--;
			right++;
		}
		// odd cases
		left = index;
		right = index + 1;
		while (left >= 0 && right < s.length && s[left] === s[right]) {
			let checked = checkSubstring(left, right, result, resultLength, s);
			[result, resultLength] = checked;
			left--;
			right++;
		}
	}
	return result;
}

function checkSubstring(
	left: number,
	right: number,
	result: string,
	resultLength: number,
	s: string
): [string, number] {
	if (right - left + 1 > resultLength) {
		result = s.slice(left, right + 1);
		resultLength = right - left + 1;
	}
	return [result, resultLength];
}
// ** command to run file: "npx ts-node longestSubstring.ts" **
console.log(longestPalindrome('babad'));

from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    try:
        data = request.get_json()
        print("GOT FROM JS:",data)
        numbers = data['array']
        target = data['target']
        
        start = time.time()
        bubble_nums=numbers.copy()
        n=len(bubble_nums)
        for i in range(n):
         for j in range(0,n-i-1):
            if bubble_nums[j]>bubble_nums[j+1]:
                bubble_nums[j],bubble_nums[j+1]=bubble_nums[j+1],bubble_nums[j]
            bubble_time=time.time()-start
        
       
        # Merge Sort - using Python's sorted()
        start = time.time()
        sorted_nums = sorted(numbers)
        merge_time = time.time() - start
        
        # Linear Search
        start = time.time()
        linear_found = target in numbers
        linear_time = time.time() - start
        
        # Binary Search
        start = time.time()
        low, high = 0, len(sorted_nums) - 1
        binary_found = False
        while low <= high:
            mid = (low + high) // 2
            if sorted_nums[mid] == target:
                binary_found = True
                break
            elif sorted_nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        binary_time = time.time() - start
        
        # These key names MUST be: bubble, merge, linear, binary
        result = {
            "bubble": f"{bubble_time:.8f}",
            "merge": f"{merge_time:.8f}", 
            "linear": f"{linear_time:.8f} | Found: {linear_found}",
            "binary": f"{binary_time:.8f} | Found: {binary_found}"
        }
        print("SENDING TO JS:", result)
        return jsonify(result)
        
    except Exception as e:
     print("ERROR:",str(e))
     return jsonify({"error": str(e)}), 400

if __name__== '__main__':
    app.run(host="0.0.0.0", port=10000)

# Universal Turing Machine
**RWU Software design**<br>
Jason Giroux<br>
James Lee<br>
Will Manley<br>

### Prerequisites:
NPM/ NODE: https://nodejs.org/en/download/ <br>
Python: https://www.python.org/downloads/ <br>

# Running Source Code
### Setup/ Deployment:
```git clone https://github.com/jaysongiroux/universalturingmachine```
<br>
```cd universalturingmachine```
### Setting up dependancies:
```npm i python-shell```
### Setting up node:
```npm install ```
### Starting the program:
```npm start```

# Running From Executable: 
- Packaged together using Electron-Packager: https://www.npmjs.com/package/electron-packager <br>
- Download the zip file from: https://drive.google.com/file/d/11VVDGymV3cND15r3Lg1tLaLYfeQK0lto/view?usp=sharing 
- Extract Folder and open folder that Corresponds to your operating system.
## Options:
1.	Mac (Darwin)
2.	Win 64


# Examples:
1. **Example 1:** a\*b\* - Tape must start at the first character in the tape and be bounded on both sides <br>
    **Tape:** [,>a,a,a,a,a,b,b,b,b,]
2. **Example 2:** (a+b)\*c+a\* - Tape must start at the first character in the tape and must be bounded on both sides <br>
    **Tape:** [,>a,b,a,b,a,b,a,b,a,b,a,b,a,b,c,a,]
3. **Example 3:** a's in multiples of 3's - Tape must start at the first character in the tape and must be bounded on both sides <br>
    **Tape:** [,>a,a,a,]
4. **Example 4:**  Accepts: c a\* b\* Δ\* '[SPACE]'\* c, tape can start wherever within bounds. Tape must be bounded on both sides. Accepts both forms of a "space" <br>
    **Tape:** [,c,a,b,>a,c,] or [,c,a,b,>Δ,c,]

# Input:
### Tape:
**Example Format:** "[,>a,b,c,Δ, ,a,b,c,a,b,c"<br>
- Brackets must be seperated from the tape by commas as seen from the format example above.
- Spaces can be represented as Δ or " " as long as it is consistent within the tape and transitions

### Transitions:
**Example Format:** "{q0,a,q1,b,R},{q1,c,q2,b,L}"
- {current state, read, goto state, movement}

# Output:
### Logging:
In this tab, you can trace the turing machine and follow the movements. With this output it makes it easy for the user to trace the position of the read head and determine the actions it is making.
### Encoding:
  When the encoding functions were designed, we purposed it to not be limited to a small alphabet. The table below is how each character is decoded. Between characters, there is a trailing "0".<br>
  To encode numbers, there is a sense of logic involved. since the only reason to involve numbers is when writing states (for example, "q5"). There is the same number of 1's as the number that follows "q" 


 <table>
        <thead>
        <tr>
            <th>Letter/ Symbol</th>
            <th>Encoding Number</th>
        </tr>
        </thead>
        <tbody style="font-size: 11px">
        <tr>
            <td>a</td>
            <td>1</td>
        </tr>
        <tr>
            <td>b</td>
            <td>11</td>
        </tr>
        <tr>
            <td>c</td>
            <td>111</td>
        </tr>
        <tr>
            <td>c</td>
            <td>111</td>
        </tr>
        <tr>
            <td>d</td>
            <td>1111</td>
        </tr>
        <tr>
            <td>e</td>
            <td>11111</td>
        </tr>
        <tr>
            <td>f</td>
            <td>111111</td>
        </tr>
        <tr>
            <td>g</td>
            <td>1111111</td>
        </tr>
        <tr>
            <td>h</td>
            <td>11111111</td>
        </tr>
        <tr>
            <td>i</td>
            <td>111111111</td>
        </tr>
        <tr>
            <td>j</td>
            <td>1111111111</td>
        </tr>
        <tr>
            <td>k</td>
            <td>11111111111</td>
        </tr>
        <tr>
            <td>l</td>
            <td>111111111111</td>
        </tr>
        <tr>
            <td>m</td>
            <td>1111111111111</td>
        </tr>
        <tr>
            <td>n</td>
            <td>11111111111111</td>
        </tr>
        <tr>
            <td>o</td>
            <td>111111111111111</td>
        </tr>
        <tr>
            <td>p</td>
            <td>1111111111111111</td>
        </tr>
        <tr>
            <td>q</td>
            <td>11111111111111111</td>
        </tr>
        <tr>
            <td>r</td>
            <td>111111111111111111</td>
        </tr>
        <tr>
            <td>s</td>
            <td>1111111111111111111</td>
        </tr>
        <tr>
            <td>t</td>
            <td>11111111111111111111</td>
        </tr>
        <tr>
            <td>u</td>
            <td>111111111111111111111</td>
        </tr>
        <tr>
            <td>v</td>
            <td>1111111111111111111111</td>
        </tr>
        <tr>
            <td>w</td>
            <td>11111111111111111111111</td>
        </tr>
        <tr>
            <td>x</td>
            <td>111111111111111111111111</td>
        </tr>
        <tr>
            <td>y</td>
            <td>1111111111111111111111111</td>
        </tr>
        <tr>
            <td>z</td>
            <td>11111111111111111111111111</td>
        </tr>
        <tr>
            <td>Δ or Space</td>
            <td>111111111111111111111111111</td>
        </tr>
        <tr>
            <td>-</td>
            <td>1111111111111111111111111111</td>
        </tr>
        <tr>
            <td>[</td>
            <td>11111111111111111111111111111</td>
        </tr>
        <tr>
            <td>]</td>
            <td>111111111111111111111111111111</td>
        </tr>



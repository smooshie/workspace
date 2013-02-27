import sys
from numpy import NaN, Inf, arange, isscalar, array, asarray

def peakdet(v, delta, x = None):
    """
    Converted from MATLAB script at http://billauer.co.il/peakdet.html
    
    Returns two arrays
    
    function [maxtab, mintab]=peakdet(v, delta, x)
    %PEAKDET Detect peaks in a vector
    %        [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
    %        maxima and minima ("peaks") in the vector V.
    %        MAXTAB and MINTAB consists of two columns. Column 1
    %        contains indices in V, and column 2 the found values.
    %      
    %        With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
    %        in MAXTAB and MINTAB are replaced with the corresponding
    %        X-values.
    %
    %        A point is considered a maximum peak if it has the maximal
    %        value, and was preceded (to the left) by a value lower by
    %        DELTA.
    
    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.
    
    """
    maxtab = []
    mintab = []
       
    if x is None:
        x = arange(len(v))
    
    v = asarray(v)
    
    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')
    
    if not isscalar(delta):
        sys.exit('Input argument delta must be a scalar')
    
    if delta <= 0:
        sys.exit('Input argument delta must be positive')
    
    mn, mx = Inf, -Inf
    mnpos, mxpos = NaN, NaN
    
    lookformax = True
    
    for i in arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]
        
        if lookformax:
            if this < mx-delta:
                if this < v[i+1]:
                    continue
                else:
                    maxtab.append((mxpos, mx))
                    mn = this
                    mnpos = x[i]
                    lookformax = False
        else:
            if this > mn+delta:
                if this > v[i+1]:
                    continue
                else:
                    mintab.append((mnpos, mn))
                    mx = this
                    mxpos = x[i]
                    lookformax = True

    return array(maxtab), array(mintab)

if __name__=="__main__":
    
    sorted = open("coverage_mapped.txt", "r")
    sorted12 = open("coverage_mapped12.txt", "r")
    
    sorteds = []
    sortedp = []
    
    for line in sorted:
        part = line.split()
        sorteds.append(int(part[2]))
    
    for line in sorted12:
        part = line.split()
        sortedp.append(int(part[2]))
    
    sorted.close()
    sorted12.close()
    
    paired_max = open("paired_max.txt", "w")
    paired_min = open("pairted_min.txt", "w")
    singles_max = open("singles_max.txt", "w")
    singles_min = open("singles_min.txt", "w")    
        
    #series = [0,0,0,2,0,0,0,-2,0,0,0,2,0,0,0,-2,0]
    maxtab, mintab = peakdet(sortedp,20)
    paired_max.write('\n'.join([' '.join(str(entry) for entry in inner) for inner in maxtab]))
    paired_min.write('\n'.join([' '.join(str(entry) for entry in inner) for inner in mintab]))   
    paired_max.close()
    paired_min.close()
     
    maxtab, mintab = peakdet(sorteds,20)
    singles_max.write('\n'.join([' '.join(str(aaa) for aaa in aa) for aa in maxtab]))
    singles_min.write('\n'.join([' '.join(str(aaa) for aaa in aa) for aa in mintab]))    
    singles_max.close()
    singles_min.close()
  
    '''
    plot(series)
    scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')
    scatter(array(mintab)[:,0], array(mintab)[:,1], color='red')
    '''

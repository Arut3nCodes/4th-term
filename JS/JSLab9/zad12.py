from ChildrenClasses import *

if __name__ == '__main__':
    accPassClass = PasswordAcceptedEntry('Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2')
    denPassClass = PasswordDeniedEntry('Dec 10 07:08:30 LabSZ sshd[24208]: Failed password for invalid user webmaster from 173.234.31.186 port 39257 ssh2')
    errorInfClass = ErrorEntry('Dec 10 11:03:40 LabSZ sshd[25448]: error: Received disconnect from 103.99.0.122: 14: No more user authentication methods available. [preauth]')
    otherInfClass = OtherInformationEntry('Dec 10 11:03:45 LabSZ sshd[25459]: Invalid user user')

    print(f'{type(accPassClass)} || {repr(accPassClass)}')
    print(f'{type(denPassClass)} || {repr(denPassClass)}')
    print(f'{type(errorInfClass)} || {repr(errorInfClass)}')
    print(f'{type(otherInfClass)} || {repr(otherInfClass)}')
    print('-'*40)
    print(accPassClass.returnIP())
    print(otherInfClass.returnIP())

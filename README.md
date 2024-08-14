# `Project Connect`
  - this is mine.
# error help.
  -  Services.msc를 열고 "Remote Procedure Call (RPC)" 서비스가 실행 중인지 확인하세요. 이 서비스가 중지되었거나 비활성화되었으면, 이를 실행하고 자동 시작으로 설정하세요.
  -  방화벽 예외 추가: 원격 컴퓨터의 Windows 방화벽에서 RPC 트래픽을 허용해야 합니다. 기본적으로 방화벽에서 원격 명령을 차단할 수 있기 때문에, 다음 포트를 방화벽에서 허용해야 합니다.
       - TCP 135번 포트: RPC Endpoint Mapper가 사용하는 포트입니다.
       - TCP 445번 포트: SMB over TCP가 사용하는 포트로, 원격 컴퓨터 관리에 사용됩니다.
  - 네트워크 설정: Windows 컴퓨터의 "네트워크 및 공유 센터"에서 네트워크가 공용이 아닌, **"프라이빗 네트워크"**로 설정되어 있는지 확인하세요.
  - 컴퓨터 관리 -> 사용자 및 그룹 -> 그룹에서 사용자가 로컬 관리자 그룹에 포함되어 있는지 확인하세요.원격 관리 권한 부여: 원격 컴퓨터에서 원격 관리를 허용하도록 설정되어 있는지 확인하세요. 이를 위해 "시스템 속성" -> "원격" 탭으로 가서 **"원격 관리"**를 활성화하세요.
  - WinRM (Windows Remote Management) 활성화: 원격 명령을 실행하기 위해 원격 컴퓨터에서 WinRM이 활성화되어 있는지 확인하세요. WinRM이 활성화되어 있지 않으면 다음 명령어를 관리자 권한으로 실행해 활성화하세요: winrm quickconfig
  - 위의 모든 설정을 적용한 후, PowerShell을 사용해 명령어가 정상적으로 실행되는지 테스트하세요: Test-Connection -ComputerName "RemoteComputerName"

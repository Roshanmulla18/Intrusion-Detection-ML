import pyshark

def capture_live_packets(packet_count=5, interface='Wi-Fi'):
    print(f"[INFO] Capturing {packet_count} packets on interface '{interface}'...")
    capture = pyshark.LiveCapture(interface=interface)

    for packet in capture.sniff_continuously(packet_count=packet_count):
        print(packet)

if __name__ == "__main__":
    capture_live_packets()

#!/usr/bin/env python3
"""
Script to run DRC and LVS using OpenRAM technology rules
"""

import os
import subprocess
import sys

def find_klayout():
    """Find KLayout installation"""
    possible_paths = [
        "/Applications/KLayout/klayout.app/Contents/MacOS/klayout",
        "/usr/local/bin/klayout",
        "/opt/homebrew/bin/klayout",
        "klayout"
    ]
    
    for path in possible_paths:
        result = subprocess.run(['which', path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    
    return None

def run_drc_with_klayout(gds_file, drc_rule_file, output_report="drc_report.lyrdb"):
    """Run DRC using KLayout and the specified rule file"""
    print(f"🔍 Running DRC with KLayout...")
    print(f"  GDS file: {gds_file}")
    print(f"  DRC rules: {drc_rule_file}")
    print(f"  Output: {output_report}")
    
    klayout_path = find_klayout()
    if not klayout_path:
        print("❌ KLayout not found!")
        print("Please install KLayout: brew install klayout")
        return False
    
    # Create KLayout command
    cmd = [
        klayout_path,
        "-b",  # batch mode
        "-r", drc_rule_file,
        "-rd", f"input={gds_file}",
        "-rd", f"output={output_report}"
    ]
    
    print(f"Running: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✅ DRC completed successfully")
            if os.path.exists(output_report):
                print(f"📊 DRC report saved to: {output_report}")
            return True
        else:
            print("❌ DRC failed")
            print("Error:", result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ DRC timed out")
        return False
    except Exception as e:
        print(f"❌ Error running DRC: {e}")
        return False

def run_lvs_with_klayout(gds_file, lvs_rule_file, spice_file, output_report="lvs_report.lyrdb"):
    """Run LVS using KLayout"""
    print("🔍 Running LVS with KLayout...")
    print(f"  GDS file: {gds_file}")
    print(f"  LVS rules: {lvs_rule_file}")
    print(f"  SPICE file: {spice_file}")
    print(f"  Output: {output_report}")
    
    klayout_path = find_klayout()
    if not klayout_path:
        print("❌ KLayout not found!")
        print("Please install KLayout: brew install klayout")
        return False
    
    # Get absolute paths to avoid path construction issues
    abs_gds_file = os.path.abspath(gds_file)
    abs_spice_file = os.path.abspath(spice_file)
    abs_output_report = os.path.abspath(output_report)
    
    # Create KLayout command with absolute paths
    cmd = [
        klayout_path,
        "-b",  # batch mode
        "-r", lvs_rule_file,
        "-rd", f"input={abs_gds_file}",
        "-rd", f"schematic={abs_spice_file}",
        "-rd", f"report={abs_output_report}"
    ]
    
    print(f"Running: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✅ LVS completed successfully")
            if os.path.exists(output_report):
                print(f"📊 LVS report saved to: {output_report}")
            return True
        else:
            print("❌ LVS failed")
            print("Error:", result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ LVS timed out")
        return False
    except Exception as e:
        print(f"❌ Error running LVS: {e}")
        return False

def show_available_rules():
    """Show available DRC and LVS rules"""
    print("📋 Available DRC and LVS Rules:")
    print("=" * 50)
    
    technologies = ["freepdk45", "scn4m_subm", "sky130"]
    
    for tech in technologies:
        drc_file = f"technology/{tech}/tech/{tech}.lydrc"
        lvs_file = f"technology/{tech}/tech/{tech}.lylvs"
        
        print(f"\n🔧 {tech.upper()} Technology:")
        
        if os.path.exists(drc_file):
            size = os.path.getsize(drc_file)
            print(f"  ✅ DRC rules: {drc_file} ({size:,} bytes)")
        else:
            print(f"  ❌ DRC rules: {drc_file} (missing)")
            
        if os.path.exists(lvs_file):
            size = os.path.getsize(lvs_file)
            print(f"  ✅ LVS rules: {lvs_file} ({size:,} bytes)")
        else:
            print(f"  ❌ LVS rules: {lvs_file} (missing)")

def show_drc_rules_summary(drc_file):
    """Show a summary of DRC rules"""
    print(f"\n📐 DRC Rules Summary for {os.path.basename(drc_file)}:")
    print("=" * 50)
    
    try:
        with open(drc_file, 'r') as f:
            content = f.read()
        
        # Extract rule categories
        rules = {
            "WELL": content.count("WELL."),
            "POLY": content.count("POLY."),
            "ACTIVE": content.count("ACTIVE."),
            "IMPLANT": content.count("IMPLANT."),
            "CONTACT": content.count("CONTACT."),
            "METAL1": content.count("METAL1."),
            "METAL2": content.count("METAL2."),
            "VIA1": content.count("VIA1."),
            "VIA2": content.count("VIA2."),
        }
        
        total_rules = sum(rules.values())
        print(f"Total DRC rules: {total_rules}")
        
        for category, count in rules.items():
            if count > 0:
                print(f"  {category}: {count} rules")
                
    except Exception as e:
        print(f"❌ Error reading DRC file: {e}")

def show_lvs_rules_summary(lvs_file):
    """Show a summary of LVS rules"""
    print(f"\n🔌 LVS Rules Summary for {os.path.basename(lvs_file)}:")
    print("=" * 50)
    
    try:
        with open(lvs_file, 'r') as f:
            content = f.read()
        
        # Extract device types
        devices = {
            "PMOS": content.count("PMOS_"),
            "NMOS": content.count("NMOS_"),
            "Connect": content.count("connect("),
            "Extract": content.count("extract_devices"),
        }
        
        print("Device extraction rules:")
        for device, count in devices.items():
            if count > 0:
                print(f"  {device}: {count} rules")
                
    except Exception as e:
        print(f"❌ Error reading LVS file: {e}")

def main():
    print("=" * 60)
    print("OPENRAM DRC/LVS VERIFICATION TOOL")
    print("=" * 60)
    
    # Show available rules
    show_available_rules()
    
    # Your specific files
    gds_file = "tempfreepdk45spice-710/freepdk45_16x2.gds"
    spice_file = "tempfreepdk45spice-710/freepdk45_16x2.lvs.sp"
    drc_rules = "technology/freepdk45/tech/freepdk45.lydrc"
    lvs_rules = "technology/freepdk45/tech/freepdk45.lylvs"
    
    print(f"\n🎯 Your SRAM Files:")
    print(f"  GDS: {gds_file}")
    print(f"  SPICE: {spice_file}")
    print(f"  DRC Rules: {drc_rules}")
    print(f"  LVS Rules: {lvs_rules}")
    
    # Check if files exist
    missing_files = []
    for file_path in [gds_file, spice_file, drc_rules, lvs_rules]:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing files:")
        for file_path in missing_files:
            print(f"  - {file_path}")
        return
    
    print("\n✅ All required files found!")
    
    # Show rule summaries
    show_drc_rules_summary(drc_rules)
    show_lvs_rules_summary(lvs_rules)
    
    # Ask user what to run
    print("\n" + "=" * 60)
    print("VERIFICATION OPTIONS")
    print("=" * 60)
    
    print("1. Run DRC (Design Rule Check)")
    print("2. Run LVS (Layout vs Schematic)")
    print("3. Run both DRC and LVS")
    print("4. Show rule details only")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        run_drc_with_klayout(gds_file, drc_rules)
    elif choice == "2":
        run_lvs_with_klayout(gds_file, lvs_rules, spice_file)
    elif choice == "3":
        print("\n" + "=" * 60)
        print("RUNNING BOTH DRC AND LVS")
        print("=" * 60)
        run_drc_with_klayout(gds_file, drc_rules)
        print("\n" + "-" * 60)
        run_lvs_with_klayout(gds_file, lvs_rules, spice_file)
    elif choice == "4":
        print("\n📋 Manual verification commands:")
        print(f"\nDRC command:")
        print(f"klayout -b -r {drc_rules} -rd input={gds_file} -rd output=drc_report.lyrdb")
        print(f"\nLVS command:")
        print(f"klayout -b -r {lvs_rules} -rd input={gds_file} -rd schematic={spice_file} -rd report=lvs_report.lyrdb")
    else:
        print("Invalid choice!")
    
    print("\n" + "=" * 60)
    print("VERIFICATION COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main() 
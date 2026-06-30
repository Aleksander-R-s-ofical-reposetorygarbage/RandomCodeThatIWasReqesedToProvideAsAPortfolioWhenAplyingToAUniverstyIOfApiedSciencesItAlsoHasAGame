using UnityEngine;
using UnityEngine.InputSystem;


public class Move_p : MonoBehaviour
{
    private Rigidbody2D rb;    
    private Animator animator;
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        animator = GetComponent<Animator>();
    }
    public float speed_p = 12;
    public bool lock_camera = true;
    float jumpF = 11f;
    bool mj_token = false;
    private string now_anim="";

    private void C_anim(string anim)
    {
        if (now_anim != anim)
        {
            animator.Play(anim);
        }
    }
    //mv
    bool last_right=true;

    public int hero=0;
    float anim_lock=0;



    // Update is called once per frame
    void Update()
    {
        if (lock_camera==false)
        {
            if (Keyboard.current.leftArrowKey.isPressed){
                rb.linearVelocity = new Vector2(-speed_p, rb.linearVelocity.y);
            }
            else if (Keyboard.current.rightArrowKey.isPressed){
                rb.linearVelocity = new Vector2(speed_p, rb.linearVelocity.y);
            }
            else{
                rb.linearVelocity = new Vector2(0, rb.linearVelocity.y);
            }
            if (Keyboard.current.spaceKey.wasPressedThisFrame && Physics2D.Raycast(transform.position, Vector2.down, 2.1f, LayerMask.GetMask("Ground")))
            {
                rb.linearVelocity=new Vector2(rb.linearVelocity.x,jumpF);
                mj_token=true;
            }
            if (Keyboard.current.spaceKey.wasReleasedThisFrame && mj_token)
            {
                rb.linearVelocity = new Vector2(rb.linearVelocity.x, rb.linearVelocity.y * 0);
            }
            if (rb.linearVelocity.y < 0)
            {
                mj_token = false;
                rb.gravityScale=3f;
            }
            else
            {
                rb.gravityScale=1f;
            }

        if (anim_lock < 0)
        {
            if (Keyboard.current.qKey.isPressed){
                hero = 0;
            }
            else if (Keyboard.current.wKey.isPressed)
                {
                    hero=1;
                }
            else if (Keyboard.current.eKey.isPressed)
                {
                    hero=2;
                }
            else if (Keyboard.current.rKey.isPressed)
                {
                    hero=3;
                }
            if (rb.linearVelocity.x > 0)
                {
                    last_right=true;
                }
            else if(rb.linearVelocity.x < 0)
                {
                    last_right=false;
                }
            if (last_right)
            {
                //if last direction was right
            switch (hero)
            {
            case 0:
                if (Keyboard.current.zKey.wasPressedThisFrame)
                    {
                        C_anim("H1_a_s_r");
                        anim_lock=16/Time.deltaTime/30;
                    }
                    else if (Keyboard.current.xKey.wasPressedThisFrame)
                        {
                            C_anim("H1_a_ax_r");
                            anim_lock=20/Time.deltaTime/30;
                        }
                        else if (Keyboard.current.cKey.wasPressedThisFrame)
                        {
                            C_anim("H1_a_g_r");
                            anim_lock=20/Time.deltaTime/30;
                        }
                        else if (mj_token)
                        {
                            C_anim("H1_j_r");
                        }
                        else if(rb.linearVelocity.x != 0)
                        {
                            C_anim("H1_mv_l");
                        }
                        else
                        {
                            C_anim("H1fix1");
                        }
            break;
            case 1:
                if (Keyboard.current.zKey.wasPressedThisFrame)
                    {
                        C_anim("H2_a_s_r");
                        anim_lock=16/Time.deltaTime/30;
                    }
                    else if (Keyboard.current.xKey.wasPressedThisFrame)
                        {
                            C_anim("H2_a_ax_r");
                            anim_lock=20/Time.deltaTime/30;
                        }
                        else if (Keyboard.current.cKey.wasPressedThisFrame)
                        {
                            C_anim("H2_a_g_r");
                            anim_lock=20/Time.deltaTime/30;
                        }
                        else if (mj_token)
                        {
                            C_anim("H2_j_r");
                        }
                        else if(rb.linearVelocity.x != 0)
                        {
                            C_anim("H2_mv_r");
                        }
                        else
                        {
                            C_anim("H2_idle_r");
                        }
            break;
            case 2:
                if (Keyboard.current.zKey.wasPressedThisFrame)
                    {
                        C_anim("H4_a_s_r");
                        anim_lock=14/Time.deltaTime/30;
                    }
                    else if (Keyboard.current.xKey.wasPressedThisFrame)
                        {
                            C_anim("H4_a_ax_r");
                            anim_lock=18/Time.deltaTime/30;
                        }
                        else if (Keyboard.current.cKey.wasPressedThisFrame)
                        {
                            C_anim("H4_a_g_r");
                            anim_lock=18/Time.deltaTime/30;
                        }
                        else if(rb.linearVelocity.x != 0)
                        {
                            C_anim("H4_mv_r");
                        }
                        else
                        {
                            C_anim("H4_idle_r");
                        }
            break;
            case 3:
                if (Keyboard.current.zKey.wasPressedThisFrame)
                    {
                        C_anim("H4_a_s_r_u");
                        anim_lock=10/Time.deltaTime/30;
                    }
                    else if (Keyboard.current.xKey.wasPressedThisFrame)
                        {
                            C_anim("H4_a_ax_r_u");
                            anim_lock=13/Time.deltaTime/30;
                        }
                        else if (Keyboard.current.cKey.wasPressedThisFrame)
                        {
                            C_anim("H4_a_g_r_u");
                            anim_lock=13/Time.deltaTime/30;
                        }
                        else if(rb.linearVelocity.x != 0)
                        {
                            C_anim("H4_mv_r_u");
                        }
                        else
                        {
                            C_anim("H4_idle_r_u");
                        }
                break;
            }               
            }
                    else
                    {
            switch (hero)
            {
                case 0:
                if (Keyboard.current.zKey.wasPressedThisFrame)
                    {
                        C_anim("H1_a_s_l");
                        anim_lock=16/Time.deltaTime/30;
                    }
                    else if (Keyboard.current.xKey.wasPressedThisFrame)
                        {
                            C_anim("H1_a_ax_l");
                            anim_lock=20/Time.deltaTime/30;
                        }
                        else if (Keyboard.current.cKey.wasPressedThisFrame)
                        {
                            C_anim("H1_a_g_l");
                            anim_lock=20/Time.deltaTime/30;
                        }
                        else if (mj_token)
                        {
                            C_anim("H1_j_l");
                        }
                        else if(rb.linearVelocity.x != 0)
                        {
                            C_anim("H1_mv_r");
                        }
                        else
                        {
                            C_anim("H1_idle_l_fix");
                        }
            break;
            case 1:
                if (Keyboard.current.zKey.wasPressedThisFrame)
                    {
                        C_anim("H2_a_s_l");
                        anim_lock=16/Time.deltaTime/30;
                    }
                    else if (Keyboard.current.xKey.wasPressedThisFrame)
                        {
                            C_anim("H2_a_ax_l");
                            anim_lock=20/Time.deltaTime/30;
                        }
                        else if (Keyboard.current.cKey.wasPressedThisFrame)
                        {
                            C_anim("H2_a_g_l");
                            anim_lock=20/Time.deltaTime/30;
                        }
                        else if (mj_token)
                        {
                            C_anim("H2_j_l");
                        }
                        else if(rb.linearVelocity.x != 0)
                        {
                            C_anim("H2_mv_l");
                        }
                        else
                        {
                            C_anim("H2_idle_l");
                        }
            break;
            case 2:
                if (Keyboard.current.zKey.wasPressedThisFrame)
                    {
                        C_anim("H4_a_s_l");
                        anim_lock=14/Time.deltaTime/30;
                    }
                    else if (Keyboard.current.xKey.wasPressedThisFrame)
                        {
                            C_anim("H4_a_ax_l");
                            anim_lock=18/Time.deltaTime/30;
                        }
                        else if (Keyboard.current.cKey.wasPressedThisFrame)
                        {
                            C_anim("H4_a_g_l");
                            anim_lock=18/Time.deltaTime/30;
                        }
                        else if(rb.linearVelocity.x != 0)
                        {
                            C_anim("H4_mv_l");
                        }
                        else
                        {
                            C_anim("H4_idle_l");
                        }
            break;
            case 3:
                if (Keyboard.current.zKey.wasPressedThisFrame)
                    {
                        C_anim("H4_a_s_l_u");
                        anim_lock=10/Time.deltaTime/30;
                    }
                    else if (Keyboard.current.xKey.wasPressedThisFrame)
                        {
                            C_anim("H4_a_ax_l_u");
                            anim_lock=13/Time.deltaTime/30;
                        }
                        else if (Keyboard.current.cKey.wasPressedThisFrame)
                        {
                            C_anim("H4_a_g_l_u");
                            anim_lock=13/Time.deltaTime/30;
                        }
                        else if(rb.linearVelocity.x != 0)
                        {
                            C_anim("H4_mv_l_u");
                        }
                        else
                        {
                            C_anim("H4_idle_l_u");
                        }
            break;
            }               
                }
        }
        else
        {
            anim_lock--;
            return;
        }
        }
    }

    
}
